from django.db import models

# Create your models here.
class mouse_species(models.Model): ##for sam,vistar,sd,n2,etc
    specie_name=models.CharField(max_length=30)

class mouse_type(models.Model):  ##for quarantine ,pup,exp,breeding,etc
    type_name=models.CharField(max_length=30)

