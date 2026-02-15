from django.db import models

# Create your models here.


class Servicetable(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "servicetable"
        verbose_name_plural = "Servicetable"

    def __str__(self):
        return self.name