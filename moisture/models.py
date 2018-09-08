import datetime
from lxml import etree
from uuid import uuid4
from django.db import models

# Create your models here.


class MoistureModel(models.Model):

    # Choices

    ATT4P = '4.3'
    ATT1P = '4.4'
    ATT_METHOD_CHOICES = (
        (ATT4P, '4 Point (Definitive)'),
        (ATT1P, '1 Point'),
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

    PREP1 = '1'
    PREP2 = '2'
    PREP3 = '3'
    PREPARATION_METHOD_CHOICES = (
        (PREP1, 'Natural Condition'),
        (PREP2, '>425um removed by hand'),
        (PREP3, '>425um removed by washing'),
    )

    # Model fields

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project_id = models.CharField(verbose_name='Project number', max_length=8)
    hole_id = models.CharField(verbose_name='Hole number', max_length=8)
    depth_top = models.DecimalField(verbose_name='Top depth (m)', max_digits=6, decimal_places=2, blank=True, null=True)
    sample_type = models.CharField(verbose_name='Sample type', max_length=4)
    technician = models.CharField(verbose_name='Technician name', max_length=32)
    att_method = models.CharField(verbose_name='Test method', max_length=3, choices=ATT_METHOD_CHOICES, default=ATT4P)
    balance = models.CharField(verbose_name='Balance used', max_length=7, choices=BALANCE_CHOICES, blank=True)
    penetrometer = models.CharField(max_length=7, default='ATT-004')
    test_date = models.DateField(auto_now_add=True)
    preparation_method = models.CharField(verbose_name='Preparation method', max_length=1, choices=PREPARATION_METHOD_CHOICES, blank=True)
    oven = models.CharField(verbose_name='Oven used', max_length=7, choices=OVEN_CHOICES, blank=True)
    oven_temp = models.IntegerField(verbose_name='Oven temperature (degrees celcius)', blank=True, null=True)
    sieve_total = models.DecimalField(verbose_name='Total mass before sieving (grams)', max_digits=6, decimal_places=2, blank=True, null=True)
    sieve_retained = models.DecimalField(verbose_name='Mass retained on 425um sieve (grams)', max_digits=6, decimal_places=2, blank=True, null=True)

    # Methods

    @staticmethod
    def generate_xml(att_test, pretty_print=True, utf=8, definitions=True):
        conversion = {"att_method": "1Pointor4Point", #
                      "check_cal": "AppCheckCal", #
                      "check_tip": "AppCheckTip", #
                      "check_vis": "AppCheckVis", #
                      "balance": "BalanceNumber", #
                      "test_date": "DateOfTest", #
                      "penetrometer": "LlPenetrometerNumber", #
                      "sieve_retained": "MassRetained425Sieve", #
                      "oven": "OvenNumber", # 
                      "oven_temp": "OvenTemperature", # 
                      }
        
        root = etree.Element("keylab", 
                     content="schedule", 
                     timestamp=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), 
                     xmlns="http://www.keynetix.com/XSD/KeyLAB/Export")

        if definitions:
            test_defs = etree.SubElement(root, "test-definitions")
            test_def = etree.SubElement(test_defs, "test-definition", name="Atterberg 4 Point", code="ATT4P")
            properties = etree.SubElement(test_def, "properties")

            for key in conversion:
                etree.SubElement(properties, "property", name=conversion[key], unit="")

        project = etree.SubElement(root, "project", id="Unknown", name="Unknown")
        samples = etree.SubElement(project, "samples")
        sample = etree.SubElement(samples, "sample", id="Unknown")
        test = etree.SubElement(sample, "test", code="ATT4P", specimen="1")
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