from django.db import models

# Create your models here. Format to store the data in the database and specifying their datatype
class ItemsList(models.Model):
    items_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=(('food','food'), ('sports','sports')))
    subcategory = models.CharField(max_length=20, choices=(('vegetables','vegetables'), ('fruit','fruit'), ('cricket','cricket'), ('football','football')))
    amount = models.IntegerField()

    objects = models.Manager()         # in views it was giving error