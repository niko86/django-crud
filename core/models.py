from django.db import models


class ProjectModel(models.Model):
    project_id = models.CharField(unique=True, verbose_name='Project number', max_length=8)


class LocationModel(models.Model):
    hole_id = models.CharField(verbose_name='Hole number', max_length=8)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='locations', related_query_name='location')


class SampleModel(models.Model):
    depth_top = models.DecimalField(verbose_name='Top depth (m)', max_digits=6, decimal_places=2, blank=True, null=True)
    sample_type = models.CharField(verbose_name='Sample type', max_length=4)
    location = models.ForeignKey(LocationModel, on_delete=models.CASCADE, related_name='samples', related_query_name='sample')


class TestModel(models.Model):
    pass
