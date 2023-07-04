from netbox.search import SearchIndex, register_search
from .models import NASCluster, NASVolume, NASShare, NASMount

@register_search
class NASClusterIndex(SearchIndex):
  model = NASCluster
  fields = (
    ('name', 100),
    ('description', 500),
  )

@register_search
class NASVolumeIndex(SearchIndex):
  model = NASVolume
  fields = (
    ('name', 100),
    ('owner', 100),
    ('group', 100),
    ('local_directory', 500),
    ('description', 500),
  )

@register_search
class NASShareIndex(SearchIndex):
  model = NASShare
  fields = (
    ('name', 100),
    ('volume_subdirectory', 500),
    ('description', 500),
  )

@register_search
class NASMountIndex(SearchIndex):
  model = NASMount
  fields = (
    ('local_directory', 500),
    ('description', 500),
  )
