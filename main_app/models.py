from django.db import models

# Create your models here.
class Spices(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    cuisine = models.CharField(max_length=300)
    shelf_life = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    spice = models.ForeignKey(Spices, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.name