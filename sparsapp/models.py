from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save


from PIL import Image
from django.conf import settings
import os

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200) 
    start_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    week_number = models.CharField(max_length=2, blank=True)
    end_date = models.DateField()

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1]
        super().save(*args, **kwargs)





class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    admire=models.ManyToManyField("self",related_name="admired_by",symmetrical=False,
        blank=True)
    
    profile_image = models.ImageField(null=True,blank=True, upload_to="images/")
    profile_bio = models.CharField(null=True,blank=True,max_length=3000)
    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=profile(user=instance)
        user_profile.save()
        user_profile.admire.set([instance.profile.id])
        user_profile.save()
post_save.connect(create_profile, sender=User)

class wallet(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    ticker=models.CharField(max_length=200,null=True,blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # Quantity of stocks owned
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at which stocks were purchased
    date_purchased = models.DateField() 

    class Meta:
        db_table='wallet'

    def __str__(self):
        return self.user.username

def create_wallet(sender,instance,created,**kwargs):
    user_wallet=wallet(user=instance)
    user_wallet.save()

class otp(models.Model):
    user=models.CharField(max_length=200,null=False,blank=False)
    email=models.CharField(max_length=200,null=False,blank=False)
    otp=models.CharField(max_length=8,null=False,blank=False)
    class Meta:
        db_table='otp'


class paydata(models.Model):
    paypurchase_price = models.DecimalField(max_digits=10, decimal_places=2)
      # Price at which stocks were purchased
    class Meta:
        db_table='paydata'

