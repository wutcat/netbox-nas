from django import forms
from ipam.models import Prefix, IPAddress
from dcim.models import Device
from virtualization.models import VirtualMachine
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
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

    class Meta:
        model = NASCluster
        fields = ('name', 'description', 'devices', 'access_ips')

class NASClusterFilterForm(NetBoxModelFilterSetForm):
    model = NASCluster
    name = forms.CharField(
        required=False
    )
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )

class NASVolumeForm(NetBoxModelForm):
    class Meta:
        model = NASVolume
        fields = ('nas_cluster', 'name', 'export_id', 'owner', 'group', 'size_gb', 'local_directory', 'security_style', 'base_unix_permissions', 'description')

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

class NASShareForm(NetBoxModelForm):
    access_prefixes = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        required=False
    )
    access_ips = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        required=False
    )

    class Meta:
        model = NASShare
        fields = ('nas_volume', 'name', 'type', 'access_level', 'access_prefixes', 'access_ips', 'mount_options', 'description')

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

class NASMountForm(NetBoxModelForm):
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False
    )

    class Meta:
        model = NASMount
        fields = ('nas_share', 'local_directory', 'devices', 'virtual_machines', 'mount_options')

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
