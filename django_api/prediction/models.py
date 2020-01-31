# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Activity(models.Model):
    SPORT = models.FloatField()
    SKIN = models.FloatField()
    HEIGHT = models.FloatField()
    AGE = models.FloatField()
    WEIGHT = models.FloatField()
    chest_Temp = models.FloatField()
    chest_EDA = models.FloatField()
    chest_EMG = models.FloatField()
    chest_ECG = models.FloatField()
    chest_ACC_Z = models.FloatField()
    chest_ACC_X = models.FloatField()
    chest_ACC_Y = models.FloatField()
    EDA = models.FloatField()
    wrist_ACC_Z = models.FloatField()
    wrist_ACC_X = models.FloatField()
    wrist_ACC_Y = models.FloatField()
    pred_activity = models.FloatField(null=True)

