from django.conf.urls import include, url
from api_app.views import BroastViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'broast', BroastViewSet, basename='broast')

urlpatterns = [
    url(r'api/', include(router.urls))
]