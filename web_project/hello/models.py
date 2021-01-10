from django.db import models

class Contact(models.Model): 
    name =  models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=120, null=True) 
    address = models.CharField(max_length=100, null=True) 
    state = models.CharField(max_length=100, null=True ) 
    phone = models.CharField(max_length=100, null=True )
    zip = models.CharField(max_length=11, null=True ) 
 




    def __str__(self):
        return self.name
     
    

   