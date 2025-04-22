# projects/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField()
    technologies = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
