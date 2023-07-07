from rest_framework import serializers
from tenancy.api.serializers import NestedTenantSerializer
from ipam.api.serializers import NestedPrefixSerializer, NestedIPAddressSerializer
from dcim.api.serializers import NestedDeviceSerializer
from virtualization.api.serializers import NestedVirtualMachineSerializer
from ipam.models import Prefix, IPAddress
from dcim.models import Device
from virtualization.models import VirtualMachine
from netbox.api.fields import SerializedPKRelatedField
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import NASCluster, NASVolume, NASShare, NASMount

class NestedNASClusterSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nascluster-detail'
    )
    access_ips = SerializedPKRelatedField(
        queryset=IPAddress.objects.all(),
        serializer=NestedIPAddressSerializer,
        required=False,
        many=True
    )

    class Meta:
        model = NASCluster
        fields = ('id', 'url', 'display', 'name', 'access_ips')

class NestedNASVolumeSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasvolume-detail'
    )

    class Meta:
        model = NASVolume
        fields = ('id', 'url', 'display', 'name', 'export_id', 'owner', 'group', 'size_gb', 'local_directory')

class NestedNASShareSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasshare-detail'
    )

    class Meta:
        model = NASShare
        fields = ('id', 'url', 'display', 'name', 'volume_subdirectory', 'mount_options', 'type', 'access_level', 'description')

class NestedNASMountSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasmount-detail'
    )

    class Meta:
        model = NASMount
        fields = ('id', 'url', 'display')

class NASClusterSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nascluster-detail'
    )
    devices = SerializedPKRelatedField(
        queryset=Device.objects.all(),
        serializer=NestedDeviceSerializer,
        required=False,
        many=True
    )
    access_ips = SerializedPKRelatedField(
        queryset=IPAddress.objects.all(),
        serializer=NestedIPAddressSerializer,
        required=False,
        many=True
    )
    tenant = NestedTenantSerializer()

    class Meta:
        model = NASCluster
        fields = ('id', 'url', 'display', 'name', 'devices', 'access_ips', 'description', 'tenant')

class NASVolumeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasvolume-detail'
    )
    tenant = NestedTenantSerializer()
    nas_cluster = NestedNASClusterSerializer()

    class Meta:
        model = NASVolume
        fields = ('id', 'url', 'display', 'name', 'export_id', 'owner', 'group', 'size_gb', 'local_directory', 'security_style', 'base_unix_permissions', 'description', 'tenant', 'nas_cluster')

class NASShareSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasshare-detail'
    )
    tenant = NestedTenantSerializer()
    nas_volume = NestedNASVolumeSerializer

    class Meta:
        model = NASShare
        fields = ('id', 'url', 'display', 'name', 'type', 'mount_options', 'access_level', 'access_prefixes', 'access_ips', 'description', 'tenant' 'nas_volume')

class NASMountSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasmount-detail'
    )
    nas_share = NestedNASShareSerializer()
    devices = SerializedPKRelatedField(
        queryset=Device.objects.all(),
        serializer=NestedDeviceSerializer,
        required=False,
        many=True
    )
    virtual_machines = SerializedPKRelatedField(
        queryset=VirtualMachine.objects.all(),
        serializer=NestedVirtualMachineSerializer,
        required=False,
        many=True
    )
    tenant = NestedTenantSerializer()

    class Meta:
        model = NASMount
        fields = ('id', 'url', 'display', 'devices', 'virtual_machines', 'local_directory', 'mount_options', 'description', 'tenant', 'nas_share')
