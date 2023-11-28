from django.db import models

class Counter(models.Model):
    key = models.CharField(max_length=10)
    value = models.IntegerField() 
    description = models.TextField()  
    
    
class Comment(models.Model):
    item = models.ForeignKey('ItemInfo', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  
    

class ItemInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    votes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.name