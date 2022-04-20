from extras.plugins import PluginConfig

class NetBoxNASConfig(PluginConfig):
    name = 'netbox_nas'
    verbose_name = 'NetBox NAS'
    description = 'Add NAS entities to NetBox'
    version = '0.1'
    base_url = 'nas'

config = NetBoxNASConfig
