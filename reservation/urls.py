from django.conf.urls import url
from rest_framework import routers
from .views import ReservationViewSet

router = routers.DefaultRouter()
router.register(r'reservation', ReservationViewSet)

urlpatterns = router.urls
