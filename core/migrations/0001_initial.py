# Generated by Django 2.1.1 on 2018-09-13 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hole_id', models.CharField(max_length=8, verbose_name='Hole number')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=8, unique=True, verbose_name='Project number')),
            ],
        ),
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth_top', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Top depth (m)')),
                ('sample_type', models.CharField(max_length=4, verbose_name='Sample type')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', related_query_name='sample', to='core.LocationModel')),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='locationmodel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', related_query_name='location', to='core.ProjectModel'),
        ),
    ]
