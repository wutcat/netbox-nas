from netbox.plugins import PluginMenuButton, PluginMenuItem

nascluster_buttons = [
    PluginMenuButton(
        link='plugins:netbox_nas:nascluster_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    ),
]
nasvolume_buttons = [
    PluginMenuButton(
        link='plugins:netbox_nas:nasvolume_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]
nasshare_buttons = [
    PluginMenuButton(
        link='plugins:netbox_nas:nasshare_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]
nasmount_buttons = [
    PluginMenuButton(
        link='plugins:netbox_nas:nasmount_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]

menu_items=(
    PluginMenuItem(
        link='plugins:netbox_nas:nascluster_list',
        link_text='NAS Clusters',
        buttons=nascluster_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_nas:nasvolume_list',
        link_text='NAS Volumes',
        buttons=nasvolume_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_nas:nasshare_list',
        link_text='NAS Shares',
        buttons=nasshare_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_nas:nasmount_list',
        link_text='NAS Mounts',
        buttons=nasmount_buttons
    )
)
