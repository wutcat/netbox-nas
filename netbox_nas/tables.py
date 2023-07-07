import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import NASCluster, NASVolume, NASShare, NASMount

class NASClusterTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    devices = tables.ManyToManyColumn(
        linkify_item=True
    )
    access_ips = tables.ManyToManyColumn(
        linkify_item=True
    )
    tenant = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = NASCluster
        fields = ('pk', 'id', 'name', 'devices', 'access_ips', 'tenant')
        default_columns = ('name', 'devices', 'access_ips', 'tenant')

class NASVolumeTable(NetBoxTable):
    nas_cluster = tables.Column(
        linkify=True
    )
    name = tables.Column(
        linkify=True
    )
    tenant = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = NASVolume
        fields = ('pk', 'id', 'name', 'export_id', 'owner', 'group', 'size_gb', 'local_directory', 'nas_cluster', 'security_style', 'base_unix_permissions', 'description', 'tenant')
        default_columns = ('name', 'export_id', 'owner', 'group', 'size_gb', 'local_directory', 'tenant', 'nas_cluster')

class NASShareTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    nas_volume = tables.Column(
        linkify=True
    )
    access_prefixes = tables.ManyToManyColumn(
        linkify_item=True
    )
    access_ips = tables.ManyToManyColumn(
        linkify_item=True
    )
    tenant = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = NASShare
        fields = ('pk', 'id', 'name', 'type', 'access_level', 'access_prefixes', 'access_ips', 'tenant', 'nas_volume')
        default_columns = ('name', 'type', 'access_level', 'nas_volume', 'tenant')

class NASMountTable(NetBoxTable):
    nas_share = tables.Column(
        linkify=True
    )
    devices = tables.ManyToManyColumn(
        linkify_item=True
    )
    virtual_machines = tables.ManyToManyColumn(
        linkify_item=True
    )
    tenant = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = NASMount
        fields = ('pk', 'id', 'local_directory', 'tenant', 'nas_share', 'devices', 'virtual_machines')
        default_columns = ('id', 'local_directory', 'tenant', 'nas_share', 'devices', 'virtual_machines')
