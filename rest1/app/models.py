from django.db import models

# Create your models here.

# class Item(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.FloatField()
#     quantity = models.PositiveIntegerField()

class Bucketlist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
