from django.db import models

# Create your models here.
class Bucketlist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


    # def save(self,*args,**kwargs):
    #     if self._state.adding and self._state.db is none:
    #         with connection.cursor() as cursor:
    #             try:
    #                 cursor.execute("select add_table")
    #             else DatabaseError:
    #                 raise ValueError(self.tablename)
    #     super().save(*args, **kwargs)
