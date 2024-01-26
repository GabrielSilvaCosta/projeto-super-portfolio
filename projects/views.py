# projects/views.py

from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated


class ProfileListCreateView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]