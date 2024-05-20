from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox.models.features import ContactsMixin
from tenancy.models import Tenant, ContactAssignment
from ipam.models import Prefix, IPAddress
from dcim.models import Device
from utilities.choices import ChoiceSet
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField

class NASVolumeSecurityStyleChoices(ChoiceSet):
    CHOICES = [
        ('unix', 'UNIX'),
        ('windows', 'Windows'),
    ]

class NASShareTypeChoices(ChoiceSet):
    CHOICES = [
        ('nfs', 'NFS', 'orange'),
        ('smb', 'SMB/CIFS', 'green'),
        ('gpfs', 'GPFS', 'blue'),
        ('cephfs', 'CephFS', 'purple'),
    ]

class NASShareAccessLevelChoices(ChoiceSet):
    CHOICES = [
        ('rw', 'Read/Write'),
        ('ro', 'Read-Only'),
    ]

class NASCluster(ContactsMixin, NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    devices = models.ManyToManyField(
        to='dcim.Device',
        related_name='devices',
        blank=True,
        verbose_name='Devices'
    )

    access_ips = models.ManyToManyField(
        to='ipam.IPAddress',
        related_name='nas_cluster_access_ips',
        blank=True,
        verbose_name='Access IPs'
    )

    description = models.CharField(
        max_length=500,
        blank=True
    )

    comments = models.TextField(
        blank=True
    )

    tenant = models.ForeignKey(
        to=Tenant,
        on_delete=models.PROTECT,
        related_name='nas_clusters',
        blank = True,
        null = True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_nas:nascluster', args=[self.pk])

class NASVolume(ContactsMixin, NetBoxModel):
    nas_cluster = models.ForeignKey(
        to=NASCluster,
        on_delete=models.PROTECT,
        related_name='volumes'
    )

    name = models.CharField(
        max_length=100
    )

    export_id = models.PositiveIntegerField()

    owner = models.CharField(
        max_length=100
    )

    group = models.CharField(
        max_length=100
    )

    size_gb = models.PositiveIntegerField()

    local_directory = models.CharField(
        max_length=200
    )

    security_style = models.CharField(
        max_length=30,
        choices=NASVolumeSecurityStyleChoices,
        default='unix'
    )

    base_unix_permissions = models.CharField(
        max_length=100,
        default='2770'
    )

    description = models.CharField(
        max_length=500,
        blank=True
    )

    comments = models.TextField(
        blank=True
    )

    tenant = models.ForeignKey(
        to=Tenant,
        on_delete=models.PROTECT,
        related_name='nas_volumes',
        blank = True,
        null = True
    )

    class Meta:
        ordering = ('nas_cluster', 'local_directory')
        unique_together = (
            ('nas_cluster', 'local_directory'),
            ('nas_cluster', 'export_id'),
        )

    def __str__(self):
        return f'{self.nas_cluster}: {self.local_directory}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_nas:nasvolume', args=[self.pk])

class NASShare(ContactsMixin, NetBoxModel):
    nas_volume = models.ForeignKey(
        to=NASVolume,
        on_delete=models.PROTECT,
        related_name='shares'
    )

    name = models.CharField(
        max_length=50
    )

    volume_subdirectory = models.CharField(
        max_length=200,
        default='/'
    )

    type = models.CharField(
        max_length=30,
        choices=NASShareTypeChoices
    )

    mount_options = models.CharField(
        max_length=100,
        blank=True
    )

    access_level = models.CharField(
        max_length=30,
        choices=NASShareAccessLevelChoices,
        default='rw'
    )

    access_prefixes = models.ManyToManyField(
        to='ipam.Prefix',
        related_name='nas_share_access_prefixes',
        blank=True,
        verbose_name='Access Prefixes'
    )

    access_ips = models.ManyToManyField(
        to='ipam.IPAddress',
        related_name='nas_share_access_ips',
        blank=True,
        verbose_name='Access IPs'
    )

    description = models.CharField(
        max_length=500,
        blank=True
    )

    comments = models.TextField(
        blank=True
    )

    tenant = models.ForeignKey(
        to=Tenant,
        on_delete=models.PROTECT,
        related_name='nas_shares',
        blank = True,
        null = True
    )

    class Meta:
        ordering = ('nas_volume', 'name')
        unique_together = ('nas_volume', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_nas:nasshare', args=[self.pk])

class NASMount(ContactsMixin, NetBoxModel):
    nas_share = models.ForeignKey(
        to=NASShare,
        on_delete=models.PROTECT,
        related_name='mounts'
    )

    devices = models.ManyToManyField(
        to='dcim.Device',
        related_name='nas_mount_devices',
        blank=True,
        verbose_name='Devices'
    )

    virtual_machines = models.ManyToManyField(
        to='virtualization.VirtualMachine',
        related_name='nas_mount_virtual_machines',
        blank=True,
        verbose_name='Virtual Machines'
    )

    local_directory = models.CharField(
        max_length=200
    )

    mount_options = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.CharField(
        max_length=500,
        blank=True
    )

    comments = models.TextField(
        blank=True
    )

    tenant = models.ForeignKey(
        to=Tenant,
        on_delete=models.PROTECT,
        related_name='nas_mounts',
        blank = True,
        null = True
    )

    class Meta:
        ordering = ('nas_share', 'local_directory')
        unique_together = ('nas_share', 'local_directory')

    def __str__(self):
        return f'{self.nas_share}: {self.local_directory}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_nas:nasmount', args=[self.pk])
