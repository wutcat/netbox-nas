from netbox.filtersets import NetBoxModelFilterSet
from .models import NASCluster, NASVolume, NASShare, NASMount

class NASFilterSet(NetBoxModelFilterSet):
    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)

class NASClusterFilterSet(NASFilterSet):
    class Meta:
        model = NASCluster
        fields = ('id', 'name', 'tenant', 'tag', 'devices')

class NASVolumeFilterSet(NASFilterSet):
    class Meta:
        model = NASVolume
        fields = ('id', 'nas_cluster', 'name', 'local_directory', 'owner', 'group', 'security_style', 'tenant', 'tag')

class NASShareFilterSet(NASFilterSet):
    class Meta:
        model = NASShare
        fields = ('id', 'nas_volume', 'name', 'type', 'access_level', 'access_prefixes', 'access_ips', 'tenant', 'tag')

class NASMountFilterSet(NASFilterSet):
    class Meta:
        model = NASMount
        fields = ('id', 'nas_share', 'devices', 'virtual_machines', 'local_directory', 'tenant', 'tag')
