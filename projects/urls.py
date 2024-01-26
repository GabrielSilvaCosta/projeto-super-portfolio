# projects/urls.py
from rest_framework import routers
from django.urls import include, path

from projects.views import ProfileListCreateView, ProjectListCreateView


router = routers.DefaultRouter()
router.register("profiles", ProfileListCreateView)
router.register("projects", ProjectListCreateView)

urlpatterns = [
    path("", include(router.urls)),
]
