# projects/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer


class ProfileListCreateView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "retrieve" and self.request.method == "GET":
            return [AllowAny()]
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if request.method == "GET":
            return render(
                request, "profile_detail.html", {"profile": serializer.data}
            )
        return super().retrieve(request, *args, **kwargs)


class ProjectListCreateView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
