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

    class Meta(NetBoxTable.Meta):
        model = NASCluster
        fields = ('pk', 'id', 'name', 'devices')
        default_columns = ('name', 'devices')

class NASVolumeTable(NetBoxTable):
    cluster = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = NASVolume
        fields = ('pk', 'id', 'owner_uid', 'group_gid', 'size_gb', 'local_directory', 'nas_cluster')
        default_columns = ('id', 'owner_uid', 'group_gid', 'size_gb', 'local_directory', 'nas_cluster')

class NASShareTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    nas_volume = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = NASShare
        fields = ('pk', 'id', 'name', 'type', 'nas_volume')
        default_columns = ('name', 'type', 'nas_volume')

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
    prefixes = tables.ManyToManyColumn(
        linkify_item=True
    )

    class Meta(NetBoxTable.Meta):
        model = NASMount
        fields = ('pk', 'id', 'local_directory', 'nas_share', 'devices', 'virtual_machines', 'prefixes')
        default_columns = ('id', 'local_directory', 'nas_share', 'devices', 'virtual_machines', 'prefixes')
