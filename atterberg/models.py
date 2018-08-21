import datetime
from lxml import etree
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
    identifier = models.CharField(verbose_name='Test identifier', max_length=64)
    att_method = models.CharField(verbose_name='Test method', max_length=3, choices=ATT_METHOD_CHOICES, default=ATT4P)
    check_cal = models.BooleanField(verbose_name='Equipment calibrations checked', blank=False, default=False)
    check_tip = models.BooleanField(verbose_name='Cone tip check complete', blank=False, default=False)
    check_vis = models.BooleanField(verbose_name='Visual sieve check complete', blank=False, default=False)
    balance = models.CharField(verbose_name='Balance used', max_length=7, choices=BALANCE_CHOICES, blank=True)
    penetrometer = models.CharField(max_length=7, default='ATT-004')
    test_date = models.DateField(auto_now_add=True)
    preparation_method = models.CharField(verbose_name='Preparation method', max_length=1, choices=PREPARATION_METHOD_CHOICES, blank=True)
    oven = models.CharField(verbose_name='Oven used', max_length=7, choices=OVEN_CHOICES, blank=True)
    oven_temp = models.IntegerField(verbose_name='Oven temperature (degrees celcius)', blank=True)
    sieve_total = models.DecimalField(verbose_name='Total mass before sieving (grams)', max_digits=6, decimal_places=2, blank=True)
    sieve_retained = models.DecimalField(verbose_name='Mass retained on 425um sieve (grams)', max_digits=6, decimal_places=2, blank=True)
    pl1_con = models.CharField(verbose_name='Plastic limit 1: Container ID', max_length=8, blank=True)
    pl1_con_mass = models.DecimalField(verbose_name='Plastic limit 1: Container mass (grams)', max_digits=6, decimal_places=2, blank=True)
    pl1_wet_mass = models.DecimalField(verbose_name='Plastic limit 1: Wet mass (grams)', max_digits=6, decimal_places=2, blank=True)
    pl1_dry1_mass = models.DecimalField(verbose_name='Plastic limit 1: First dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    pl1_dry2_mass = models.DecimalField(verbose_name='Plastic limit 1: Second dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    pl2_con = models.CharField(verbose_name='Plastic limit 2: Container ID', max_length=8, blank=True)
    pl2_con_mass = models.DecimalField(verbose_name='Plastic limit 2: Container mass (grams)', max_digits=6, decimal_places=2, blank=True)
    pl2_wet_mass = models.DecimalField(verbose_name='Plastic limit 2: Wet mass (grams)', max_digits=6, decimal_places=2, blank=True)
    pl2_dry1_mass = models.DecimalField(verbose_name='Plastic limit 2: First dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    pl2_dry2_mass = models.DecimalField(verbose_name='Plastic limit 2: Second dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll1_pene_1 = models.DecimalField(verbose_name='Liquid limit 1: Penetration 1 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll1_pene_2 = models.DecimalField(verbose_name='Liquid limit 1: Penetration 2 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll1_pene_3 = models.DecimalField(verbose_name='Liquid limit 1: Penetration 3 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll1_con = models.CharField(verbose_name='Liquid limit 1: Container ID', max_length=8, blank=True)
    ll1_con_mass = models.DecimalField(verbose_name='Liquid limit 1: Container mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll1_wet_mass = models.DecimalField(verbose_name='Liquid limit 1: Wet mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll1_dry1_mass = models.DecimalField(verbose_name='Liquid limit 1:First dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll1_dry2_mass = models.DecimalField(verbose_name='Liquid limit 1:Second dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll2_pene_1 = models.DecimalField(verbose_name='Liquid limit 2: Penetration 1 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll2_pene_2 = models.DecimalField(verbose_name='Liquid limit 2: Penetration 2 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll2_pene_3 = models.DecimalField(verbose_name='Liquid limit 2: Penetration 3 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll2_con = models.CharField(verbose_name='Liquid limit 2: Container ID', max_length=8, blank=True)
    ll2_con_mass = models.DecimalField(verbose_name='Liquid limit 2: Container mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll2_wet_mass = models.DecimalField(verbose_name='Liquid limit 2: Wet mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll2_dry1_mass = models.DecimalField(verbose_name='Liquid limit 2:First dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll2_dry2_mass = models.DecimalField(verbose_name='Liquid limit 2:Second dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll3_pene_1 = models.DecimalField(verbose_name='Liquid limit 3: Penetration 1 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll3_pene_2 = models.DecimalField(verbose_name='Liquid limit 3: Penetration 2 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll3_pene_3 = models.DecimalField(verbose_name='Liquid limit 3: Penetration 3 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll3_con = models.CharField(verbose_name='Liquid limit 3: Container ID', max_length=8, blank=True)
    ll3_con_mass = models.DecimalField(verbose_name='Liquid limit 3: Container mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll3_wet_mass = models.DecimalField(verbose_name='Liquid limit 3: Wet mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll3_dry1_mass = models.DecimalField(verbose_name='Liquid limit 3:First dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll3_dry2_mass = models.DecimalField(verbose_name='Liquid limit 3:Second dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll4_pene_1 = models.DecimalField(verbose_name='Liquid limit 4: Penetration 1 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll4_pene_2 = models.DecimalField(verbose_name='Liquid limit 4: Penetration 2 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll4_pene_3 = models.DecimalField(verbose_name='Liquid limit 4: Penetration 3 (mm)', max_digits=3, decimal_places=1, blank=True)
    ll4_con = models.CharField(verbose_name='Liquid limit 4: Container ID', max_length=8, blank=True)
    ll4_con_mass = models.DecimalField(verbose_name='Liquid limit 4: Container mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll4_wet_mass = models.DecimalField(verbose_name='Liquid limit 4: Wet mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll4_dry1_mass = models.DecimalField(verbose_name='Liquid limit 4:First dry mass (grams)', max_digits=6, decimal_places=2, blank=True)
    ll4_dry2_mass = models.DecimalField(verbose_name='Liquid limit 4:Second dry mass (grams)', max_digits=6, decimal_places=2, blank=True)

    # Methods

    @staticmethod
    def generate_xml(att_test):
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
                      "pl1_con_mass": "Pl1ContainerMass", #
                      "pl1_wet_mass": "Pl1MassContainerAndWetSoil", #
                      "pl1_dry1_mass": "Pl1FirstMassOfContainerAndDrySoil", #
                      "pl1_dry2_mass": "Pl1SecondMassOfContainerAndDrySoil", #
                      "pl2_con_mass": "Pl2ContainerMass", #
                      "pl2_wet_mass": "Pl2MassContainerAndWetSoil", #
                      "pl2_dry1_mass": "Pl2FirstMassOfContainerAndDrySoil", #
                      "pl2_dry2_mass": "Pl2SecondMassOfContainerAndDrySoil", #
                      "preparation_method": "PreparationMethodControl", #
                      "sieve_total": "TotalMassOfSample", #
                      "ll1_pene_1": "Ll1Penetration1", #
                      "ll1_pene_2": "Ll1Penetration2", #
                      "ll1_pene_3": "Ll1Penetration3", #
                      "ll1_con_mass": "Ll1ContainerMass", #
                      "ll1_wet_mass": "Ll1MassContainerAndWetSoil", #
                      "ll1_dry1_mass": "Ll1FirstMassOfContainerAndDrySoil", #
                      "ll1_dry2_mass": "Ll1SecondMassOfContainerAndDrySoil", #
                      "ll2_pene_1": "Ll2Penetration1", #
                      "ll2_pene_2": "Ll2Penetration2", #
                      "ll2_pene_3": "Ll2Penetration3", #
                      "ll2_con_mass": "Ll2ContainerMass", #
                      "ll2_wet_mass": "Ll2MassContainerAndWetSoil", #
                      "ll2_dry1_mass": "Ll2FirstMassOfContainerAndDrySoil", #
                      "ll2_dry2_mass": "Ll2SecondMassOfContainerAndDrySoil", #
                      "ll3_pene_1": "ll3Penetration1", #
                      "ll3_pene_2": "ll3Penetration2", #
                      "ll3_pene_3": "ll3Penetration3", #
                      "ll3_con_mass": "ll3ContainerMass", #
                      "ll3_wet_mass": "ll3MassContainerAndWetSoil", #
                      "ll3_dry1_mass": "ll3FirstMassOfContainerAndDrySoil", #
                      "ll3_dry2_mass": "ll3SecondMassOfContainerAndDrySoil", #
                      "ll4_pene_1": "ll4Penetration1", #
                      "ll4_pene_2": "ll4Penetration2", #
                      "ll4_pene_3": "ll4Penetration3", #
                      "ll4_con_mass": "ll4ContainerMass", #
                      "ll4_wet_mass": "ll4MassContainerAndWetSoil", #
                      "ll4_dry1_mass": "ll4FirstMassOfContainerAndDrySoil", #
                      "ll4_dry2_mass": "ll4SecondMassOfContainerAndDrySoil", #
                      }
        
        root = etree.Element("keylab", 
                     content="schedule", 
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
                getattr(att_test, item) # answer to my prayer, get attribute from passing in object and string variable of the key
            except:
                pass
            else:
                reading = etree.SubElement(readings, "reading")
                measurement = etree.SubElement(reading, "measurement", name=conversion[item], value=str(getattr(att_test, item)))
        
        return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="utf-16")