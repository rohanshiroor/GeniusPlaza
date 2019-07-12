# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=500,null=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Step(models.Model):
    step_text =  models.CharField(max_length=500,null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    def __str__(self):
        return self.step_text

class Ingredient(models.Model):
    text = models.CharField(max_length=500,null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

