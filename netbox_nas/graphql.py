from typing import Annotated, List, Union

import strawberry
import strawberry_django

from netbox.graphql.scalars import BigInt
from netbox.graphql.types import BaseObjectType, NetBoxObjectType, OrganizationalObjectType
from netbox.graphql.filter_mixins import autotype_decorator, BaseFilterMixin

from . import filtersets, models

@strawberry_django.filter(models.NASCluster, lookups=True)
@autotype_decorator(filtersets.NASClusterFilterSet)
class NASClusterFilter(BaseFilterMixin):
    pass

@strawberry_django.filter(models.NASVolume, lookups=True)
@autotype_decorator(filtersets.NASVolumeFilterSet)
class NASVolumeFilter(BaseFilterMixin):
    pass

@strawberry_django.filter(models.NASShare, lookups=True)
@autotype_decorator(filtersets.NASShareFilterSet)
class NASShareFilter(BaseFilterMixin):
    pass

@strawberry_django.filter(models.NASMount, lookups=True)
@autotype_decorator(filtersets.NASMountFilterSet)
class NASMountFilter(BaseFilterMixin):
    pass

@strawberry_django.type(
    models.NASCluster,
    fields='__all__',
    filters=NASClusterFilter,
)
class NASClusterType(NetBoxObjectType):
    _name: str
    access_ips: List[Annotated["IPAddressType", strawberry.lazy('ipam.graphql.types')]] | None
    devices: List[Annotated["DeviceType", strawberry.lazy('dcim.graphql.types')]] | None
    tenant: Annotated["TenantType", strawberry.lazy('tenancy.graphql.types')] | None
    volumes: List[Annotated["NASVolumeType", strawberry.lazy('.graphql')]] | None

@strawberry_django.type(
    models.NASVolume,
    fields='__all__',
    filters=NASVolumeFilter,
)
class NASVolumeType(NetBoxObjectType):
    nas_cluster: Annotated["NASClusterType", strawberry.lazy('.graphql')] | None
    tenant: Annotated["TenantType", strawberry.lazy('tenancy.graphql.types')] | None
    shares: List[Annotated["NASShareType", strawberry.lazy('.graphql')]] | None

@strawberry_django.type(
    models.NASShare,
    fields='__all__',
    filters=NASShareFilter,
)
class NASShareType(NetBoxObjectType):
    nas_volume: Annotated["NASVolumeType", strawberry.lazy('.graphql')] | None
    tenant: Annotated["TenantType", strawberry.lazy('tenancy.graphql.types')] | None
    mounts: List[Annotated["NASMountType", strawberry.lazy('.graphql')]] | None
    access_prefixes: List[Annotated["PrefixType", strawberry.lazy('ipam.graphql.types')]] | None
    access_ips: List[Annotated["IPAddressType", strawberry.lazy('ipam.graphql.types')]] | None

@strawberry_django.type(
    models.NASMount,
    fields='__all__',
    filters=NASMountFilter,
)
class NASMountType(NetBoxObjectType):
    nas_share: Annotated["NASShareType", strawberry.lazy('.graphql')] | None
    devices: List[Annotated["DeviceType", strawberry.lazy('dcim.graphql.types')]] | None
    virtual_machines: List[Annotated["VirtualMachineType", strawberry.lazy('virtualization.graphql.types')]] | None
    tenant: Annotated["TenantType", strawberry.lazy('tenancy.graphql.types')] | None


@strawberry.type
class NASQuery:
    @strawberry.field
    def nascluster(self, id: int) -> NASClusterType:
        return models.NASCluster.objects.get(pk=id)
    nascluster_list: list[NASClusterType] = strawberry_django.field()

    def nasvolume(self, id: int) -> NASVolumeType:
        return models.NASVolume.objects.get(pk=id)
    nasvolume_list: list[NASVolumeType] = strawberry_django.field()

    def nasshare(self, id: int) -> NASShareType:
        return models.NASShare.objects.get(pk=id)
    nasshare_list: list[NASShareType] = strawberry_django.field()

    def nasmount(self, id: int) -> NASMountType:
        return models.NASMount.objects.get(pk=id)
    nasmount_list: list[NASMountType] = strawberry_django.field()

schema = [
    NASQuery,
]
