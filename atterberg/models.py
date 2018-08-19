from uuid import uuid4
from django.db import models

# Create your models here.
class AttModel(models.Model):

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

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    att_method = models.CharField(verbose_name='Test method', max_length=3, choices=ATT_METHOD_CHOICES, default=ATT4P)
    check_cal = models.BooleanField(verbose_name='Equipment calibrations checked', blank=False, default=False)
    check_tip = models.BooleanField(verbose_name='Cone tip check complete', blank=False, default=False)
    check_vis = models.BooleanField(verbose_name='Visual sieve check complete', blank=False, default=False)
    balance = models.CharField(verbose_name='Balance used', max_length=7, choices=BALANCE_CHOICES, default='BAL-001')
    test_date = models.DateField(auto_now_add=True)
    preparation_method = models.CharField(verbose_name='Preparation method', max_length=1, choices=PREPARATION_METHOD_CHOICES, default=PREP1)
