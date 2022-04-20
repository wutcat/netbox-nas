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
)
