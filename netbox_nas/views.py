from django.db.models import Count
from netbox.views import generic
from tenancy.views import ObjectContactsView
from ipam.tables import PrefixTable, IPAddressTable
from dcim.tables import DeviceTable
from virtualization.tables import VirtualMachineTable
from utilities.views import register_model_view
from . import filtersets, forms, models, tables

# NAS Clusters
class NASClusterView(generic.ObjectView):
    queryset = models.NASCluster.objects.all()

    def get_extra_context(self, request, instance):
        volumes_table = tables.NASVolumeTable(instance.volumes.all())
        volumes_table.configure(request)
        devices_table = DeviceTable(instance.devices.all())
        devices_table.configure(request)
        access_ips_table = IPAddressTable(instance.access_ips.all())
        access_ips_table.configure(request)

        return {
            'volumes_table': volumes_table,
            'devices_table': devices_table,
            'access_ips_table': access_ips_table,
        }

@register_model_view(models.NASCluster, 'contacts')
class NASClusterContactsView(ObjectContactsView):
    queryset = models.NASCluster.objects.all()

class NASClusterListView(generic.ObjectListView):
    queryset = models.NASCluster.objects.all()
    table = tables.NASClusterTable
    filterset = filtersets.NASClusterFilterSet
    filterset_form = forms.NASClusterFilterForm

class NASClusterEditView(generic.ObjectEditView):
    queryset = models.NASCluster.objects.all()
    form = forms.NASClusterForm

class NASClusterDeleteView(generic.ObjectDeleteView):
    queryset = models.NASCluster.objects.all()


# NAS Volumes
class NASVolumeView(generic.ObjectView):
    queryset = models.NASVolume.objects.all()

    def get_extra_context(self, request, instance):
        shares_table = tables.NASShareTable(instance.shares.all())
        shares_table.configure(request)

        return {
            'shares_table': shares_table,
        }

@register_model_view(models.NASVolume, 'contacts')
class NASVolumeContactsView(ObjectContactsView):
    queryset = models.NASVolume.objects.all()

class NASVolumeListView(generic.ObjectListView):
    queryset = models.NASVolume.objects.all()
    table = tables.NASVolumeTable
    filterset = filtersets.NASVolumeFilterSet
    filterset_form = forms.NASVolumeFilterForm

class NASVolumeEditView(generic.ObjectEditView):
    queryset = models.NASVolume.objects.all()
    form = forms.NASVolumeForm

class NASVolumeDeleteView(generic.ObjectDeleteView):
    queryset = models.NASVolume.objects.all()


# NAS Shares
class NASShareView(generic.ObjectView):
    queryset = models.NASShare.objects.all()

    def get_extra_context(self, request, instance):
        mounts_table = tables.NASMountTable(instance.mounts.all())
        mounts_table.configure(request)
        prefixes_table = PrefixTable(instance.access_prefixes.all())
        prefixes_table.configure(request)
        ips_table = IPAddressTable(instance.access_ips.all())
        ips_table.configure(request)

        return {
            'mounts_table': mounts_table,
            'prefixes_table': prefixes_table,
            'ips_table': ips_table,
        }

@register_model_view(models.NASShare, 'contacts')
class NASShareContactsView(ObjectContactsView):
    queryset = models.NASShare.objects.all()

class NASShareListView(generic.ObjectListView):
    queryset = models.NASShare.objects.all()
    table = tables.NASShareTable
    filterset = filtersets.NASShareFilterSet
    filterset_form = forms.NASShareFilterForm

class NASShareEditView(generic.ObjectEditView):
    queryset = models.NASShare.objects.all()
    form = forms.NASShareForm

class NASShareDeleteView(generic.ObjectDeleteView):
    queryset = models.NASShare.objects.all()


# NAS Mounts
class NASMountView(generic.ObjectView):
    queryset = models.NASMount.objects.all()

    def get_extra_context(self, request, instance):
        devices_table = DeviceTable(instance.devices.all())
        devices_table.configure(request)
        virtual_machines_table = VirtualMachineTable(instance.virtual_machines.all())
        virtual_machines_table.configure(request)

        return {
            'devices_table': devices_table,
            'virtual_machines_table': virtual_machines_table,
        }

@register_model_view(models.NASMount, 'contacts')
class NASMountContactsView(ObjectContactsView):
    queryset = models.NASMount.objects.all()

class NASMountListView(generic.ObjectListView):
    queryset = models.NASMount.objects.all()
    table = tables.NASMountTable
    filterset = filtersets.NASMountFilterSet
    filterset_form = forms.NASMountFilterForm

class NASMountEditView(generic.ObjectEditView):
    queryset = models.NASMount.objects.all()
    form = forms.NASMountForm

class NASMountDeleteView(generic.ObjectDeleteView):
    queryset = models.NASMount.objects.all()
