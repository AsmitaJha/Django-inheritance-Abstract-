from django.db import models

# Create your models here.

# There are 3 models: an abstract model (Person) and 2 subclasses (
    # a. Father which checks whether the person's father is old or not, taking True as the default value), and 
    # b. Child-which checks whether the child is an infant or not, with default value as False)
    
class Person(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    #creating an abstract model for a person having name, address, and phone as the fields
    class Meta:
        abstract=True  #This is the differentiating factor in abstract base classes. We should mention it.
        
class Father(Person):
    is_old=models.BooleanField(default=True)   #Inheriting Father model (subclass) from the Person model (abstract class). It has the three fields (name, address, and phone from Person model) and one more field 'is_old' as its own field 
    
class Child(Person):
    is_infant=models.BooleanField(default=False)
    