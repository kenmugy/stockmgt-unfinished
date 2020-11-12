from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    item_no = models.CharField(max_length=50)
    color = models.CharField( max_length=50)
    quantity = models.IntegerField("Quantity MTS",default=0 )
    opening_stck = models.IntegerField(default=0 )
    closing_stck = models.IntegerField(default=0 )
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
    issued_to = models.CharField("Issued to",max_length=50)
    phone_number = models.CharField( max_length=50, blank = True)
    last_updated = models.DateTimeField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"item: {self.item_no} | Color: {self.color}"
        