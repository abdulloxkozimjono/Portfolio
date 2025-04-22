# resumes/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    title = models.CharField(max_length=100)
    experience = models.TextField()
    skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)