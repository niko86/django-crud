import datetime
from lxml import etree
from uuid import uuid4
from django.db import models


class MoistureModel(models.Model):

    # Model fields

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project_id = models.CharField(verbose_name='Project number', max_length=8)
    hole_id = models.CharField(verbose_name='Hole number', max_length=8)
    depth_top = models.DecimalField(verbose_name='Top depth (m)', max_digits=6, decimal_places=2, blank=True, null=True)
    sample_type = models.CharField(verbose_name='Sample type', max_length=4)
    technician = models.CharField(verbose_name='Technician name', max_length=32)
