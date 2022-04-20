from django.db.models import Count
from netbox.views import generic
from dcim.tables import DeviceTable
from . import filtersets, forms, models, tables

# NAS Clusters
class NASClusterView(generic.ObjectView):
    queryset = models.NASCluster.objects.all()

    def get_extra_context(self, request, instance):
        volumes_table = tables.NASVolumeTable(instance.volumes.all())
        volumes_table.configure(request)
        devices_table = DeviceTable(instance.devices.all())
        devices_table.configure(request)

        return {
            'volumes_table': volumes_table,
            'devices_table': devices_table,
        }

class NASClusterListView(generic.ObjectListView):
    queryset = models.NASCluster.objects.all()
    table = tables.NASClusterTable

class NASClusterEditView(generic.ObjectEditView):
    queryset = models.NASCluster.objects.all()
    form = forms.NASClusterForm

class NASClusterDeleteView(generic.ObjectDeleteView):
    queryset = models.NASCluster.objects.all()

# NAS Volumes
class NASVolumeView(generic.ObjectView):
    queryset = models.NASVolume.objects.all()

    def get_extra_context(self, request, instance):
        shares_table = DeviceTable(instance.shares.all())
        shares_table.configure(request)

        return {
            'shares_table': shares_table,
        }

class NASVolumeListView(generic.ObjectListView):
    queryset = models.NASVolume.objects.all()
    table = tables.NASVolumeTable

class NASVolumeEditView(generic.ObjectEditView):
    queryset = models.NASVolume.objects.all()
    form = forms.NASVolumeForm

class NASVolumeDeleteView(generic.ObjectDeleteView):
    queryset = models.NASVolume.objects.all()
