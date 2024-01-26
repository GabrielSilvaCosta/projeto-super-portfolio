# projects/urls.py
from rest_framework import routers
from django.urls import include, path

from projects.views import (
    ProfileListCreateView,
    ProjectListCreateView,
    CertificateListCreateView,
    CertifyingInstitutionListCreateView,
)


router = routers.DefaultRouter()
router.register(r"profiles", ProfileListCreateView)
router.register(r"projects", ProjectListCreateView)
router.register(r"certificates", CertificateListCreateView)
router.register(
    r"certifying-institutions", CertifyingInstitutionListCreateView
)


urlpatterns = [
    path("", include(router.urls)),
]
