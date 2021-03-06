# Generated by Django 2.1.1 on 2018-09-27 11:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PsdModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_id', models.CharField(max_length=8, verbose_name='Project number')),
                ('hole_id', models.CharField(max_length=8, verbose_name='Hole number')),
                ('depth_top', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Top depth (m)')),
                ('sample_type', models.CharField(max_length=4, verbose_name='Sample type')),
                ('technician', models.CharField(max_length=32, verbose_name='Technician name')),
                ('test_date', models.DateField(auto_now_add=True)),
                ('check_cal', models.BooleanField(default=False, verbose_name='Equipment calibrations checked?')),
                ('check_vis', models.BooleanField(default=False, verbose_name='Visual sieve check complete?')),
                ('test_method', models.CharField(blank=True, choices=[('1', 'Wet sieve'), ('2', 'Dry sieve')], max_length=1, verbose_name='Test method')),
                ('description', models.CharField(max_length=256, verbose_name='Specimen description')),
                ('remarks', models.CharField(max_length=256, verbose_name='Test remarks')),
                ('natural_condition', models.BooleanField(default=False, verbose_name='Tested at received moisture content?')),
                ('dried_condition', models.BooleanField(default=False, verbose_name='Tested in pre-dried condition?')),
                ('container_id', models.CharField(max_length=8, verbose_name='Container ID')),
                ('container_mass', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Container mass (g)')),
                ('initial_wet_mass', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Initial wet mass (g)')),
                ('initial_dry_mass', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Initial dry mass (g)')),
                ('accepted_dry_mass', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Accepted dry mass (g)')),
                ('mass_125mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='125mm retained mass (g)')),
                ('mass_90mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='90mm retained mass (g)')),
                ('mass_75mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='75mm retained mass (g)')),
                ('mass_63mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='63mm retained mass (g)')),
                ('mass_50mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='50mm retained mass (g)')),
                ('mass_37p5mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='37.5mm retained mass (g)')),
                ('mass_28mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='28mm retained mass (g)')),
                ('mass_20mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='20mm retained mass (g)')),
                ('mass_below_20mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Total mass passing 20mm (g)')),
                ('sum_stack_1', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Total mass of first stack (g)')),
                ('riffle_mass_below_20mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Riffled mass below 20mm (g)')),
                ('dry_washed_mass', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Washed dry mass (g)')),
                ('mass_14mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='125mm retained mass (g)')),
                ('mass_10mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='90mm retained mass (g)')),
                ('mass_6p3mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='75mm retained mass (g)')),
                ('mass_below_6p3mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Total mass passing 6.3mm (g)')),
                ('sum_stack_2', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Total mass of second stack (g)')),
                ('riffle_mass_below_6p3mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Riffled mass below 6.3mm (g)')),
                ('mass_5mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='5mm retained mass (g)')),
                ('mass_3p35mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='3.35mm retained mass (g)')),
                ('mass_2mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='2mm retained mass (g)')),
                ('mass_1p18mm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='1.18mm retained mass (g)')),
                ('mass_600um', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='600um retained mass (g)')),
                ('mass_425um', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='425um retained mass (g)')),
                ('mass_300um', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='300um retained mass (g)')),
                ('mass_212um', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='212um retained mass (g)')),
                ('mass_150um', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='150um retained mass (g)')),
                ('mass_63um', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='63um retained mass (g)')),
                ('sum_stack_3', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Total mass of third stack (g)')),
            ],
        ),
    ]
