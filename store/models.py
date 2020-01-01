from django.db import models
from django.db.models import CharField
# Create your models here.

class MStore(models.Model):

    phone= models.CharField(max_length=30, null=True)

    email= models.CharField(max_length=30, null=True)

    password= models.CharField(max_length=30)

    nationality= models.CharField(max_length=20, null=True)

    state= models.CharField(max_length=20, null=True)

    lga= models.CharField(max_length=20, null=True)

    zip_code= models.CharField(max_length=10, null=True)

    Miousify_Store_Plans = (
        ('basic', 'basic'),
        ('premium', 'premium'),
        ('enterprise', 'enterprise'),
    )
    # the account that owns this store
    user_account= models.CharField(max_length=30, null=True);
    #miousify domain name
    miousify_domain_name= models.CharField(max_length=20, primary_key=True)
    # is this store active, has subscription been made
    is_active= models.BooleanField(default=False, null=True)
    # trial active
    trial_expired= models.BooleanField(default=False, null=True)
    # plan to be used for this store, required on which the basic service would be made available to access the store
    plan= CharField(max_length=15, choices= Miousify_Store_Plans)
    #store resource id
    miousify_store_resource_id= models.CharField(max_length=20)
    # when the store account was created
    created_at= models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name= models.CharField(max_length=20)
# Create your models here.
