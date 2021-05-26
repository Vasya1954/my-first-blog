from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db import models

class products(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField()
    cost = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)


class days_free(models.Model):
    pub_date = models.DateTimeField()
    number_student = models.IntegerField()
    portion = models.FloatField()
    all_portion = models.FloatField()
    prod = models.ForeignKey(
        products,
        on_delete=models.PROTECT,
        related_query_name="nam"
    )


class days_cost(models.Model):
    pub_date = models.DateTimeField()
    number_student = models.IntegerField()
    portion = models.IntegerField()
    all_portion = models.IntegerField()
    prod = models.ForeignKey(products, on_delete=models.PROTECT)
