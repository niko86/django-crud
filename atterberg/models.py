from uuid import uuid4
from django.db import models

# Create your models here.
class AttModel(models.Model):
    ATT4P = '4.3'
    ATT1P = '4.4'
    ATT_METHOD_CHOICES = (
        (ATT4P, '4 Point (Definitive)'),
        (ATT1P, '1 Point'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    att_method = models.CharField(max_length=3, choices=ATT_METHOD_CHOICES, default=ATT4P)
    