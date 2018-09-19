import datetime
from lxml import etree
from uuid import uuid4
from django.db import models


class MoistureModel(models.Model):

    # Choices

    FINE = 'BS 1377 - 2 : 1990 3.2.3.1'
    MEDIUM = 'BS 1377 - 2 : 1990 3.2.3.2'
    COARSE = 'BS 1377 - 2 : 1990 3.2.3.3'
    MC_METHOD_CHOICES = (
        (FINE, 'Fine-grained Soil'),
        (MEDIUM, 'Medium-grained Soil'),
        (COARSE, 'Coarse-grained Soil'),
    )

    BALANCE_CHOICES = (
        ('BAL-001', 'BAL-001'),
        ('BAL-003', 'BAL-003'),
        ('BAL-004', 'BAL-004'),
        ('BAL-005', 'BAL-005'),
        ('BAL-006', 'BAL-006'),
        ('BAL-007', 'BAL-007'),
        ('BAL-008', 'BAL-008'),
        ('BAL-009', 'BAL-009'),
        ('BAL-010', 'BAL-010'),
    )

    OVEN_CHOICES = (
        ('OVE-001', 'OVE-001'),
        ('OVE-002', 'OVE-002'),
        ('OVE-004', 'OVE-004'),
        ('OVE-005', 'OVE-005'),
        ('OVE-006', 'OVE-006'),
    )

    # Model fields

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project_id = models.CharField(verbose_name='Project number', max_length=8)
    hole_id = models.CharField(verbose_name='Hole number', max_length=8)
    depth_top = models.DecimalField(verbose_name='Top depth (m)', max_digits=6, decimal_places=2, blank=True, null=True)
    sample_type = models.CharField(verbose_name='Sample type', max_length=4)
    mc_method = models.CharField(verbose_name='Test method', max_length=32, choices=MC_METHOD_CHOICES, default=FINE)
    technician = models.CharField(verbose_name='Technician name', max_length=32)
    test_date = models.DateField(auto_now_add=True)
    balance = models.CharField(verbose_name='Balance used', max_length=7, choices=BALANCE_CHOICES, blank=True)
    oven = models.CharField(verbose_name='Oven used', max_length=7, choices=OVEN_CHOICES, blank=True)
    oven_temp = models.IntegerField(verbose_name='Oven temperature (degrees celcius)', blank=True, null=True)
    mc_con = models.CharField(verbose_name='Container ID', max_length=8, blank=True, null=True)
    mc_con_mass = models.DecimalField(verbose_name='Container mass (grams)', max_digits=6, decimal_places=2, blank=True, null=True)
    mc_wet_mass = models.DecimalField(verbose_name='Wet mass (grams)', max_digits=6, decimal_places=2, blank=True, null=True)
    mc_dry1_mass = models.DecimalField(verbose_name='First dry mass (grams)', max_digits=6, decimal_places=2, blank=True, null=True)
    mc_dry2_mass = models.DecimalField(verbose_name='Second dry mass (grams)', max_digits=6, decimal_places=2, blank=True, null=True)

    # Methods

    @staticmethod
    def generate_xml(mc_test, pretty_print=True, utf=8, definitions=True):
        conversion = {"mc_method": "TestMethod", #
                      "balance": "BalanceNumber", #
                      "test_date": "DateOfTest", #
                      "oven": "OvenNumber", # 
                      "oven_temp": "OvenTemperature", # 
                      "mc_con_mass": "ContainerMass", #
                      "mc_wet_mass": "MassContainerAndWetSoil", #
                      "mc_dry1_mass": "1StMassOfContainerAndDrySoil", #
                      "mc_dry2_mass": "2NdMassOfContainerAndDrySoil", #
                      }
        
        root = etree.Element("keylab", 
                     content="schedule", 
                     timestamp=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), 
                     xmlns="http://www.keynetix.com/XSD/KeyLAB/Export")

        if definitions:
            test_defs = etree.SubElement(root, "test-definitions")
            test_def = etree.SubElement(test_defs, "test-definition", name="Moisture Content", code="MC")
            properties = etree.SubElement(test_def, "properties")

            for key in conversion:
                etree.SubElement(properties, "property", name=conversion[key], unit="")

        project = etree.SubElement(root, "project", id="Unknown", name="Unknown")
        samples = etree.SubElement(project, "samples")
        sample = etree.SubElement(samples, "sample", id="Unknown")
        test = etree.SubElement(sample, "test", code="MC", specimen="1")
        general = etree.SubElement(test, "general")
        readings = etree.SubElement(general, "readings")


        for item in conversion:
            try:
                getattr(att_test, item) # answer to my prayer, get attribute from passing in object and string variable of the key
            except:
                pass
            else:
                if getattr(att_test, item) is None:
                    value = ""
                else:
                    value = str(getattr(att_test, item))
                reading = etree.SubElement(readings, "reading")
                measurement = etree.SubElement(reading, "measurement", name=conversion[item], value=value) # remember to change back to reading
        
        return etree.tostring(root, pretty_print=pretty_print, xml_declaration=True, encoding=f"utf-{utf}")