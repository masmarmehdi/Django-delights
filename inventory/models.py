from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    unit = models.CharField(max_length=5)
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name}'

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0)

    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())
    
    def __str__(self):
        return f'{self.title}'

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    quantity = models.FloatField(default=0)

    def enough(self):
        return self.quantity <= self.ingredient.quantity
    
    def __str__(self):
        return f'{self.menu_item}'

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.menu_item}'
