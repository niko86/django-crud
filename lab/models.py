from uuid import uuid4
from django.db import models

# Create your models here.

class Engineer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email_address = models.EmailField(max_length=128)

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project_id = models.CharField(max_length=7)
    project_name = models.CharField(max_length=128)
    engineer_name = models.ForeignKey('Engineer', on_delete=models.CASCADE)
