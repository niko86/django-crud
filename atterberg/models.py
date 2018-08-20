import datetime
import xml.etree.ElementTree as etree
from uuid import uuid4
from django.db import models

# Create your models here.


class AttModel(models.Model):

    # Choices

    ATT4P = '4.3'
    ATT1P = '4.4'
    ATT_METHOD_CHOICES = (
        (ATT4P, '4 Point (Definitive)'),
        (ATT1P, '1 Point'),
    )

    BALANCE_CHOICES = (
        ('BAL-001', 'BAL-001'),
        ('BAL-002', 'BAL-002'),
        ('BAL-003', 'BAL-003'),
        ('BAL-004', 'BAL-004'),
        ('BAL-005', 'BAL-005'),
        ('BAL-006', 'BAL-006'),
        ('BAL-007', 'BAL-007'),
        ('BAL-008', 'BAL-008'),
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
    att_method = models.CharField(
        verbose_name='Test method', max_length=3, choices=ATT_METHOD_CHOICES, default=ATT4P)
    check_cal = models.BooleanField(
        verbose_name='Equipment calibrations checked', blank=False, default=False)
    check_tip = models.BooleanField(
        verbose_name='Cone tip check complete', blank=False, default=False)
    check_vis = models.BooleanField(
        verbose_name='Visual sieve check complete', blank=False, default=False)
    balance = models.CharField(verbose_name='Balance used',
                               max_length=7, choices=BALANCE_CHOICES, default='BAL-001')
    test_date = models.DateField(auto_now_add=True)
    preparation_method = models.CharField(
        verbose_name='Preparation method', max_length=1, choices=PREPARATION_METHOD_CHOICES, default=PREP1)

    # Method

    @staticmethod
    def generate_xml(att_test):
        conversion = {"att_method": "1Pointor4Point",
                      "check_cal": "AppCheckCal",
                      "check_tip": "AppCheckTip",
                      "check_vis": "AppCheckVis",
                      "balance": "BalanceNumber",
                      "test_date": "DateOfTest",
                      "na": "Ll1ContainerMass",
                      "na": "Ll1MassContainerAndWetSoil",
                      "na": "Ll1FirstMassOfContainerAndDrySoil",
                      "na": "Ll1SecondMassOfContainerAndDrySoil",
                      "na": "Ll1Penetration1",
                      "na": "Ll1Penetration2",
                      "na": "LlPenetrometerNumber",
                      "na": "MassRetained425Sieve",
                      "na": "OvenNumber",
                      "na": "OvenTemperature",
                      "na": "Pl1ContainerMass",
                      "na": "Pl1MassContainerAndWetSoil",
                      "na": "Pl1FirstMassOfContainerAndDrySoil",
                      "na": "Pl1SecondMassOfContainerAndDrySoil",
                      "na": "Pl2ContainerMass",
                      "na": "Pl2MassContainerAndWetSoil",
                      "na": "Pl2FirstMassOfContainerAndDrySoil",
                      "na": "Pl2SecondMassOfContainerAndDrySoil",
                      "preparation_method": "PreparationMethodControl",
                      "na": "TotalMassOfSample", }
        
        root = etree.Element("keylab", 
                     content="results", 
                     timestamp=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), 
                     xmlns="http://www.keynetix.com/XSD/KeyLAB/Export")

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
                getattr(att_test, item)
            except:
                pass
            else:
                reading = etree.SubElement(readings, "reading")
                measurement = etree.SubElement(reading, "measurement", name=conversion[item], value=str(getattr(att_test, item)))
        
        return etree.tostring(root)