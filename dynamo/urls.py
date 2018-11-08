from django.conf.urls import url
from django.urls import path,  include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/', include('reservation.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('', include('user.urls')),
]
