from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    # NAS Clusters
    path('nascluster', views.NASClusterListView.as_view(), name='nascluster_list'),
    path('nascluster/add/', views.NASClusterEditView.as_view(), name='nascluster_add'),
    path('nascluster/<int:pk>/', views.NASClusterView.as_view(), name='nascluster'),
    path('nascluster/<int:pk>/edit/', views.NASClusterEditView.as_view(), name='nascluster_edit'),
    path('nascluster/<int:pk>/delete/', views.NASClusterDeleteView.as_view(), name='nascluster_delete'),
    path('nascluster/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nascluster_changelog', kwargs={
        'model': models.NASCluster
    }),

    # NAS Volumes
    path('nasvolume', views.NASVolumeListView.as_view(), name='nasvolume_list'),
    path('nasvolume/add/', views.NASVolumeEditView.as_view(), name='nasvolume_add'),
    path('nasvolume/<int:pk>/', views.NASVolumeView.as_view(), name='nasvolume'),
    path('nasvolume/<int:pk>/edit/', views.NASVolumeEditView.as_view(), name='nasvolume_edit'),
    path('nasvolume/<int:pk>/delete/', views.NASVolumeDeleteView.as_view(), name='nasvolume_delete'),
    path('nasvolume/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nasvolume_changelog', kwargs={
        'model': models.NASVolume
    }),

    # NAS Shares
    path('nasshare', views.NASShareListView.as_view(), name='nasshare_list'),
    path('nasshare/add/', views.NASShareEditView.as_view(), name='nasshare_add'),
    path('nasshare/<int:pk>/', views.NASShareView.as_view(), name='nasshare'),
    path('nasshare/<int:pk>/edit/', views.NASShareEditView.as_view(), name='nasshare_edit'),
    path('nasshare/<int:pk>/delete/', views.NASShareDeleteView.as_view(), name='nasshare_delete'),
    path('nasshare/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nasshare_changelog', kwargs={
        'model': models.NASVolume
    }),

    # NAS Mounts
    path('nasmount', views.NASMountListView.as_view(), name='nasmount_list'),
    path('nasmount/add/', views.NASMountEditView.as_view(), name='nasmount_add'),
    path('nasmount/<int:pk>/', views.NASMountView.as_view(), name='nasmount'),
    path('nasmount/<int:pk>/edit/', views.NASMountEditView.as_view(), name='nasmount_edit'),
    path('nasmount/<int:pk>/delete/', views.NASMountDeleteView.as_view(), name='nasmount_delete'),
    path('nasmount/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='nasmount_changelog', kwargs={
        'model': models.NASMount
    }),
)
