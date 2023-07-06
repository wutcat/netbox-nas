from django import forms
from ipam.models import Prefix, IPAddress
from dcim.models import Device
from virtualization.models import VirtualMachine
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from .models import NASCluster, NASVolume, NASShare, NASMount

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

class NASVolumeForm(NetBoxModelForm):
    class Meta:
        model = NASVolume
        fields = ('nas_cluster', 'name', 'export_id', 'owner', 'group', 'size_gb', 'local_directory', 'security_style', 'base_unix_permissions', 'description')

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
