from django.db import models

    # Create your models here.

class Account(models.Model):
    product = models.CharField(max_length=100)
    def _str_(self):
        return(f"name {product.self}")
    
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def _str_(self):
        return self.title
        