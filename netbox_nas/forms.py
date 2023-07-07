from django import forms
from tenancy.models import Tenant
from ipam.models import Prefix, IPAddress
from dcim.models import Device
from virtualization.models import VirtualMachine
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField, TagFilterField
from .models import NASCluster, NASVolume, NASShare, NASMount, NASVolumeSecurityStyleChoices, NASShareTypeChoices, NASShareAccessLevelChoices

class NASClusterForm(NetBoxModelForm):
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
    access_ips = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        required=False
    )
    comments = CommentField()
    class Meta:
        model = NASCluster
        fields = ('name', 'description', 'devices', 'tenant', 'tags', 'access_ips', 'comments')

class NASClusterFilterForm(NetBoxModelFilterSetForm):
    model = NASCluster
    name = forms.CharField(
        required=False
    )
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )
    tag = TagFilterField(model)

class NASVolumeForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = NASVolume
        fields = ('nas_cluster', 'name', 'export_id', 'owner', 'group', 'size_gb', 'local_directory', 'security_style', 'base_unix_permissions', 'description', 'tenant', 'tags', 'comments')

class NASVolumeFilterForm(NetBoxModelFilterSetForm):
    model = NASVolume
    nas_cluster = DynamicModelMultipleChoiceField(
        queryset=NASCluster.objects.all(),
        required=False
    )
    name = forms.CharField(
        required=False
    )
    owner = forms.CharField(
        required=False
    )
    group = forms.CharField(
        required=False
    )
    security_style = forms.MultipleChoiceField(
        choices=NASVolumeSecurityStyleChoices,
        required=False
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )
    tag = TagFilterField(model)

class NASShareForm(NetBoxModelForm):
    access_prefixes = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        required=False
    )
    access_ips = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        required=False
    )
    comments = CommentField()

    class Meta:
        model = NASShare
        fields = ('nas_volume', 'name', 'volume_subdirectory', 'type', 'access_level', 'access_prefixes', 'access_ips', 'mount_options', 'description', 'tenant', 'tags', 'comments')

class NASShareFilterForm(NetBoxModelFilterSetForm):
    model = NASShare
    nas_volume = DynamicModelMultipleChoiceField(
        queryset=NASVolume.objects.all(),
        required=False
    )
    name = forms.CharField(
        required=False
    )
    type = forms.MultipleChoiceField(
        choices=NASShareTypeChoices,
        required=False
    )
    access_level = forms.MultipleChoiceField(
        choices=NASShareAccessLevelChoices,
        required=False,
    )
    access_prefixes = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        required=False
    )
    access_ips = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        required=False
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )
    tag = TagFilterField(model)

class NASMountForm(NetBoxModelForm):
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False
    )
    comments = CommentField()

    class Meta:
        model = NASMount
        fields = ('nas_share', 'local_directory', 'devices', 'virtual_machines', 'mount_options', 'description', 'tenant', 'tags', 'comments')

class NASMountFilterForm(NetBoxModelFilterSetForm):
    model = NASMount
    nas_share = DynamicModelMultipleChoiceField(
        queryset=NASShare.objects.all(),
        required=False
    )
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )
    tag = TagFilterField(model)
