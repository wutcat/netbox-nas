from rest_framework import serializers
from ipam.api.serializers import NestedPrefixSerializer
from dcim.api.serializers import NestedDeviceSerializer
from dcim.models import Device
from netbox.api import SerializedPKRelatedField
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import NASCluster, NASVolume, NASShare, NASMount

class NestedNASClusterSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nascluster-detail'
    )

    class Meta:
        model = NASCluster
        fields = ('id', 'url', 'display', 'name')

class NestedNASVolumeSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasvolume-detail'
    )

    class Meta:
        model = NASVolume
        fields = ('id', 'url', 'display', 'owner_uid', 'group_gid', 'size_gb', 'local_directory')

class NestedNASShareSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasshare-detail'
    )

    class Meta:
        model = NASShare
        fields = ('id', 'url', 'display', 'name', 'type', 'description')

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

    class Meta:
        model = NASCluster
        fields = ('id', 'url', 'display', 'name', 'devices')

class NASVolumeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasvolume-detail'
    )
    nas_cluster = NestedNASClusterSerializer()

    class Meta:
        model = NASVolume
        fields = ('id', 'url', 'display', 'owner_uid', 'group_gid', 'size_gb', 'local_directory', 'description', 'nas_cluster')

class NASShareSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasshare-detail'
    )
    volume = NestedNASVolumeSerializer

    class Meta:
        model = NASShare
        fields = ('id', 'url', 'display', 'name', 'type', 'description', 'volume')

class NASMountSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_nas-api:nasmount-detail'
    )
    share = NestedNASShareSerializer()

    class Meta:
        model = NASMount
        fields = ('id', 'url', 'display', 'devices', 'virtual_machines', 'prefixes', 'local_directory', 'description', 'share')
