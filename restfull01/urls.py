from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('drones.urls', namespace='v1')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^v2/', include('drones.v2.urls', namespace='v2')),
    # url(r'^v2/api-auth/', include('rest_framework.urls', namespace='rest_framework_v2'))
]
