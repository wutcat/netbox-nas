# Generated by Django 4.0.4 on 2022-04-21 13:46

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipam', '0057_created_datetimefield'),
        ('virtualization', '0029_created_datetimefield'),
        ('extras', '0073_journalentry_tags_custom_fields'),
        ('dcim', '0153_created_datetimefield'),
    ]

    operations = [
        migrations.CreateModel(
            name='NASCluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('devices', models.ManyToManyField(blank=True, related_name='devices', to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='NASVolume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('owner_uid', models.PositiveIntegerField()),
                ('group_gid', models.PositiveIntegerField()),
                ('size_gb', models.PositiveIntegerField()),
                ('local_directory', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('nas_cluster', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='volumes', to='netbox_nas.nascluster')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('nas_cluster', 'local_directory'),
                'unique_together': {('nas_cluster', 'local_directory')},
            },
        ),
        migrations.CreateModel(
            name='NASShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('nas_volume', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shares', to='netbox_nas.nasvolume')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('nas_volume', 'name'),
                'unique_together': {('nas_volume', 'name')},
            },
        ),
        migrations.CreateModel(
            name='NASMount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('local_directory', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('devices', models.ManyToManyField(blank=True, related_name='nas_mount_devices', to='dcim.device')),
                ('nas_share', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mounts', to='netbox_nas.nasshare')),
                ('prefixes', models.ManyToManyField(blank=True, related_name='nas_mount_prefixes', to='ipam.prefix')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('virtual_machines', models.ManyToManyField(blank=True, related_name='nas_mount_virtual_machines', to='virtualization.virtualmachine')),
            ],
            options={
                'ordering': ('nas_share', 'local_directory'),
                'unique_together': {('nas_share', 'local_directory')},
            },
        ),
    ]
