from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_nas'

router = NetBoxRouter()
router.register('nasclusters', views.NASClusterViewSet)
router.register('nasvolumes', views.NASVolumeViewSet)
router.register('nasshares', views.NASShareViewSet)
router.register('nasmounts', views.NASMountViewSet)

urlpatterns = router.urls
