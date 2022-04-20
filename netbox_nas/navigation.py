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
    )
)
