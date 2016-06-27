from django.db import models
from haystack import indexes


# Create your models here.


class Offer(models.Model):
    id_offer = models.IntegerField(null=False, primary_key=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer'

    def __str__(self):
        return self.description

