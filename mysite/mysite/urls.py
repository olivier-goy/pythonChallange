from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from pythonChallange.views import StudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
