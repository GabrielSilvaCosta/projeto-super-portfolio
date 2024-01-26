# projects/urls.py
from rest_framework import routers
from django.urls import include, path

from projects.views import ProfileListCreateView


router = routers.DefaultRouter()
router.register("profiles", ProfileListCreateView)

urlpatterns = [
    path("", include(router.urls)),
]
