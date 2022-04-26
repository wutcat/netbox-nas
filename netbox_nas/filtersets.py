from netbox.filtersets import NetBoxModelFilterSet
from .models import NASCluster, NASVolume, NASShare, NASMount

class NASFilterSet(NetBoxModelFilterSet):
    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)

class NASClusterFilterSet(NASFilterSet):
    class Meta:
        model = NASCluster
        fields = ('id', 'name')

class NASVolumeFilterSet(NASFilterSet):
    class Meta:
        model = NASVolume
        fields = ('id', 'nas_cluster', 'name', 'local_directory', 'owner', 'group')

class NASShareFilterSet(NASFilterSet):
    class Meta:
        model = NASShare
        fields = ('id', 'nas_volume', 'name', 'type')

class NASMountFilterSet(NASFilterSet):
    class Meta:
        model = NASMount
        fields = ('id', 'nas_share', 'devices', 'virtual_machines', 'prefixes', 'local_directory')
