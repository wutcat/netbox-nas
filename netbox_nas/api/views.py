from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count
from .. import filtersets, models
from .serializers import NASClusterSerializer, NASVolumeSerializer, NASShareSerializer, NASMountSerializer

class NASClusterViewSet(NetBoxModelViewSet):
    queryset = models.NASCluster.objects.prefetch_related('tags')
    serializer_class = NASClusterSerializer

class NASVolumeViewSet(NetBoxModelViewSet):
    queryset = models.NASVolume.objects.prefetch_related('nas_cluster', 'tags')
    serializer_class = NASVolumeSerializer

class NASShareViewSet(NetBoxModelViewSet):
    queryset = models.NASShare.objects.prefetch_related('volume', 'tags')
    serializer_class = NASShareSerializer

class NASMountViewSet(NetBoxModelViewSet):
    queryset = models.NASMount.objects.prefetch_related('share', 'tags')
    serializer_class = NASMountSerializer
