from netbox.plugins import PluginConfig

class NetBoxNASConfig(PluginConfig):
    name = 'netbox_nas'
    verbose_name = 'NetBox NAS'
    description = 'Add NAS entities to NetBox'
    version = '1.0.4'
    base_url = 'nas'
    min_version = '3.7.8'

config = NetBoxNASConfig
