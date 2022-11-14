from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    unit = models.CharField(max_length=5)
    unit_price = models.FloatField(default=0)

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0)

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    quantity = models.FloatField(default=0)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now=True)
