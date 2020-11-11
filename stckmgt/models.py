from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    item_no = models.CharField(("ITEM NO"), max_length=50)
    color = models.CharField( max_length=50)
    quantity = models.IntegerField(default=0 )
    issue_by = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_to = models.CharField(max_length=50)
    phone_number = models.CharField( max_length=50)
    last_updated = models.DateTimeField( auto_now=False, auto_now_add=False)
