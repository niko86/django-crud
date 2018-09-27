import datetime
from lxml import etree
from uuid import uuid4
from django.db import models

# Create your models here.

class PsdModel(models.Model):

    # Choices

    WET = '1'
    DRY = '2'
    PSD_METHOD_CHOICES = (
        (WET, 'Wet sieve'),
        (DRY, 'Dry sieve'),
    )

    # Model fields

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project_id = models.CharField(verbose_name='Project number', max_length=8)
    hole_id = models.CharField(verbose_name='Hole number', max_length=8)
    depth_top = models.DecimalField(verbose_name='Top depth (m)', max_digits=6, decimal_places=2, blank=True, null=True)
    sample_type = models.CharField(verbose_name='Sample type', max_length=4)
    technician = models.CharField(verbose_name='Technician name', max_length=32)
    test_date = models.DateField(auto_now_add=True)
    check_cal = models.BooleanField(verbose_name='Equipment calibrations checked?', blank=False, default=False)
    check_vis = models.BooleanField(verbose_name='Visual sieve check complete?', blank=False, default=False)
    test_method = models.CharField(verbose_name='Test method', max_length=1, choices=PSD_METHOD_CHOICES, blank=True)
    description = models.TextField(verbose_name='Specimen description')
    remarks = models.TextField(verbose_name='Test remarks')
    natural_condition = models.BooleanField(verbose_name='Tested at received moisture content?', blank=False, default=False)
    dried_condition = models.BooleanField(verbose_name='Tested in pre-dried condition?', blank=False, default=False)

    container_id = models.CharField(verbose_name='Container ID', max_length=8)
    container_mass = models.DecimalField(verbose_name='Container mass (g)', max_digits=6, decimal_places=2, blank=True, null=True)
    initial_wet_mass = models.DecimalField(verbose_name='Initial wet mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    initial_dry_mass = models.DecimalField(verbose_name='Initial dry mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    accepted_dry_mass = models.DecimalField(verbose_name='Accepted dry mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)

    mass_125mm = models.DecimalField(verbose_name='125mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_90mm = models.DecimalField(verbose_name='90mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_75mm = models.DecimalField(verbose_name='75mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_63mm = models.DecimalField(verbose_name='63mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_50mm = models.DecimalField(verbose_name='50mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_37p5mm = models.DecimalField(verbose_name='37.5mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_28mm = models.DecimalField(verbose_name='28mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_20mm = models.DecimalField(verbose_name='20mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_below_20mm = models.DecimalField(verbose_name='Total mass passing 20mm (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    sum_stack_1 = models.DecimalField(verbose_name='Total mass of first stack (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    riffle_mass_below_20mm = models.DecimalField(verbose_name='Riffled mass below 20mm (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    dry_washed_mass = models.DecimalField(verbose_name='Washed dry mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)

    mass_14mm = models.DecimalField(verbose_name='125mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_10mm = models.DecimalField(verbose_name='90mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_6p3mm = models.DecimalField(verbose_name='75mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_below_6p3mm = models.DecimalField(verbose_name='Total mass passing 6.3mm (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    sum_stack_2 = models.DecimalField(verbose_name='Total mass of second stack (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    riffle_mass_below_6p3mm = models.DecimalField(verbose_name='Riffled mass below 6.3mm (g)', max_digits=7, decimal_places=2, blank=True, null=True)

    mass_5mm = models.DecimalField(verbose_name='5mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_3p35mm = models.DecimalField(verbose_name='3.35mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_2mm = models.DecimalField(verbose_name='2mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_1p18mm = models.DecimalField(verbose_name='1.18mm retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_600um = models.DecimalField(verbose_name='600um retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_425um = models.DecimalField(verbose_name='425um retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_300um = models.DecimalField(verbose_name='300um retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_212um = models.DecimalField(verbose_name='212um retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_150um = models.DecimalField(verbose_name='150um retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    mass_63um = models.DecimalField(verbose_name='63um retained mass (g)', max_digits=7, decimal_places=2, blank=True, null=True)
    sum_stack_3 = models.DecimalField(verbose_name='Total mass of third stack (g)', max_digits=7, decimal_places=2, blank=True, null=True)

    # Methods

    @staticmethod
    def generate_xml(psd_test, pretty_print=True, utf=16, definitions=True):
        conversion = {"test_date": "SieveDate",
                      "check_cal": "SieveCalibration",
                      "check_vis": "SieveCheck",
                      "test_method": "WetOrDrySieveControl",
                      "description": "SpecimenDescription",
                      "remarks": "SievingRemarks",
                      "natural_condition": "NaturalMaterialControl",
                      "dried_condition": "DriedMaterialControl",
                      "container_mass": "SieveMcContainerMass",
                      "initial_wet_mass": "SieveMcMassContainerAndWetSoil", # using initial dry in model for UKAS
                      "accepted_dry_mass": "SieveMcFirstMassOfContainerAndDrySoil",
                      "mass_125mm": "MassRetainedOn125MmSieve",
                      "mass_90mm": "MassRetainedOn90MmSieve",
                      "mass_75mm": "MassRetainedOn75MmSieve",
                      "mass_63mm": "MassRetainedOn63MmSieve",
                      "mass_50mm": "MassRetainedOn50MmSieve",
                      "mass_37p5mm": "MassRetainedOn37p5MmSieve",
                      "mass_28mm": "MassRetainedOn28MmSieve",
                      "mass_20mm": "MassRetainedOn20MmSieve",
                      "mass_below_20mm": "TotalMassBelow20Mm",
                      "sum_stack_1": "SumOfStack1",
                      "riffle_mass_below_20mm": "RiffledMassBelow20Mm",
                      "dry_washed_mass": "WeightDryAfterWashingRiffle1",
                      "mass_14mm": "MassRetainedOn14MmSieve",
                      "mass_10mm": "MassRetainedOn10MmSieve",
                      "mass_6p3mm": "MassRetainedOn6p3MmSieve",
                      "mass_below_6p3mm": "WeightPriorToRiffling2",
                      "sum_stack_2": "SumOfStack2",
                      "riffle_mass_below_6p3mm": "WeightAfterRiffling2",
                      "mass_5mm": "MassRetainedOn5MmSieve",
                      "mass_3p35mm": "MassRetainedOn3p35MmSieve",
                      "mass_2mm": "MassRetainedOn2MmSieve",
                      "mass_1p18mm": "MassRetainedOn1p18MmSieve",
                      "mass_600um": "MassRetainedOn0p6MmSieve",
                      "mass_425um": "MassRetainedOn0p425MmSieve",
                      "mass_300um": "MassRetainedOn0p3MmSieve",
                      "mass_212um": "MassRetainedOn0p212MmSieve",
                      "mass_150um": "MassRetainedOn0p15MmSieve",
                      "mass_63um": "MassRetainedOn0p063MmSieve",
                      "sum_stack_3": "WeightPassingLastSieve",
                      }

        root = etree.Element("keylab",
                             content="schedule",
                             timestamp=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                             xmlns="http://www.keynetix.com/XSD/KeyLAB/Export")

        if definitions:
            test_defs = etree.SubElement(root, "test-definitions")
            test_def = etree.SubElement(
                test_defs, "test-definition", name="Particle Size Distribution", code="PSD")
            properties = etree.SubElement(test_def, "properties")

            for key in conversion:
                etree.SubElement(properties, "property",
                                 name=conversion[key], unit="")

        project = etree.SubElement(root, "project", id="Unknown", name="Unknown")
        samples = etree.SubElement(project, "samples")
        sample = etree.SubElement(samples, "sample", id="Unknown")
        test = etree.SubElement(sample, "test", code="PSD", specimen="4")
        general = etree.SubElement(test, "general")
        readings = etree.SubElement(general, "readings")

        for item in conversion:
            try:
                # answer to my prayer, get attribute from passing in object and string variable of the key
                getattr(psd_test, item)
            except:
                pass
            else:
                if getattr(psd_test, item) is None:
                    value = ""
                else:
                    value = str(getattr(psd_test, item))

                reading = etree.SubElement(readings, "reading")
                measurement = etree.SubElement(reading, "measurement", name=conversion[item], value=value)

        return etree.tostring(root, pretty_print=pretty_print, xml_declaration=True, encoding=f"utf-{utf}")
