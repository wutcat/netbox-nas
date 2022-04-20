from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

nascluster_buttons = [
    PluginMenuButton(
        link='plugins:netbox_nas:nascluster_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    ),
]
nasvolume_buttons = [
    PluginMenuButton(
        link='plugins:netbox_nas:nasvolume_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
nasshare_buttons = [
    PluginMenuButton(
        link='plugins:netbox_nas:nasshare_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
nasmount_buttons = [
    PluginMenuButton(
        link='plugins:netbox_nas:nasmount_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
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
