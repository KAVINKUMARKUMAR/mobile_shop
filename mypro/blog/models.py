from django.db import models

class Product(models.Model):
    # not going to override the __init__ method here
    # the inherited constructor has been coded to support ORM

    # We just list out the attributes of Product Entity type below
    # Additionally, for every model, django automatically generates
    # an `id` attribute which will act as primary key in the db
    # We can choose to use it instead of creating one ourselves.
    
    name = models.CharField(max_length=255) # VARCHAR
    price = models.FloatField()
    desc = models.TextField(max_length=500)
    img = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()


    def __str__(self):
        return f"Product: {self.name}"