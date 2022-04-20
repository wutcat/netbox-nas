from netbox.filtersets import NetBoxModelFilterSet
from .models import NASVolume, NASShare, NASMount

class NASVolumeFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = NASVolume
        fields = ('id', 'owner_uid', 'group_gid')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
