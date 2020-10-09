from django.db import models

class Food(models.Model):
  name = models.CharField(max_length=100, unique = True)
  description = models.CharField(max_length=1000)
  density_min = models.DecimalField(max_digits=5, decimal_places=3)
  density_max = models.DecimalField(max_digits=5, decimal_places=3)
  specific_gravity_min = models.DecimalField(max_digits=5, decimal_places=3)
  specific_gravity_max = models.DecimalField(max_digits=5, decimal_places=3)

class Category(models.Model):
  name = models.CharField(max_length=100, unique = True)
  foods = models.ForeignKey(Food, default=1, on_delete=models.SET_DEFAULT)

class Count(models.Model):
  count = models.IntegerField(default=0)
  food = models.OneToOneField(Food, default=1, on_delete=models.SET_DEFAULT)