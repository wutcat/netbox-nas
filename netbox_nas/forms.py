from django import forms
from ipam.models import Prefix
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

    class Meta:
        model = NASCluster
        fields = ('name', 'description', 'devices')
        depth = 1

class NASVolumeForm(NetBoxModelForm):
    class Meta:
        model = NASVolume
        fields = ('nas_cluster', 'owner_uid', 'group_gid', 'size_gb', 'local_directory', 'description')

class NASShareForm(NetBoxModelForm):
    class Meta:
        model = NASShare
        fields = ('nas_volume', 'name', 'type', 'description')

class NASMountForm(NetBoxModelForm):
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False
    )
    prefixes = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        required=False
    )

    class Meta:
        model = NASMount
        fields = ('nas_share', 'local_directory', 'devices', 'virtual_machines', 'prefixes')
