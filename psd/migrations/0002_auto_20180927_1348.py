# Generated by Django 2.1.1 on 2018-09-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psdmodel',
            name='description',
            field=models.TextField(verbose_name='Specimen description'),
        ),
        migrations.AlterField(
            model_name='psdmodel',
            name='remarks',
            field=models.TextField(verbose_name='Test remarks'),
        ),
    ]