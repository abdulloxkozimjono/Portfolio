# resumes/views.py
from rest_framework import viewsets
from .models import Resume
from .serializers import ResumeSerializer
from rest_framework.permissions import IsAuthenticated


class ResumeViewSet(viewsets.ModelViewSet):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)