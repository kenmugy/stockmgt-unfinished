from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# from itemDb import ItemModel

# Create your models here.

# for c in Itemdb.objects.get('item_no'):
#     item_choives

item_choices = (
    ("", ""),
    ("V160YK", "V160YK"),
    ("V001YK", "V001YK"),
    ("V109YK", "V109YK"),
    ("V121YK", "V121YK"),
    ("V131YK", "V131YK"),
    ("V133YK", "V133YK"),
    ("V196YK", "V196YK"),
)

class Category(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})


class Stock(models.Model):
    item_no = models.CharField(max_length=50, choices = item_choices, blank = False, null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField( max_length=55, blank = False, null = True)
    quantity = models.IntegerField("Quantity MTS",default=0 )
    opening_stck = models.IntegerField("Quantity in Store",default=0 )
    closing_stck = models.IntegerField(default=0 )
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, null=True)
    issued_to = models.CharField("Issued to",max_length=50, blank= False)
    phone_number = models.CharField( max_length=50, blank = True)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField( auto_now=True, auto_now_add=False)
    # recieved_date = models.DateTimeField( auto_now=False, auto_now_add=False, blank=True)

    def get_absolute_url(self):
        return reverse('list')

    def __str__(self):
        return f"item: {self.item_no} | Color: {self.color}"
        