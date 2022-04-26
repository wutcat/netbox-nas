from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count
from .. import filtersets, models
from .serializers import NASClusterSerializer, NASVolumeSerializer, NASShareSerializer, NASMountSerializer

class NASClusterViewSet(NetBoxModelViewSet):
    queryset = models.NASCluster.objects.prefetch_related('tags')
    serializer_class = NASClusterSerializer
    filterset_class = filtersets.NASClusterFilterSet

class NASVolumeViewSet(NetBoxModelViewSet):
    queryset = models.NASVolume.objects.prefetch_related('nas_cluster', 'tags')
    serializer_class = NASVolumeSerializer
    filterset_class = filtersets.NASVolumeFilterSet

class NASShareViewSet(NetBoxModelViewSet):
    queryset = models.NASShare.objects.prefetch_related('nas_volume', 'tags')
    serializer_class = NASShareSerializer
    filterset_class = filtersets.NASShareFilterSet

class NASMountViewSet(NetBoxModelViewSet):
    queryset = models.NASMount.objects.prefetch_related('nas_share', 'tags')
    serializer_class = NASMountSerializer
    filterset_class = filtersets.NASMountFilterSet
