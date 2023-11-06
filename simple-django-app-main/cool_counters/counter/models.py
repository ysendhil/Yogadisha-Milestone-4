from django.db import models

class Counter(models.Model):
    key = models.CharField(max_length=10)
    value = models.IntegerField() 
    

class ItemInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


