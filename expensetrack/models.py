from django.db import models

# Create your models here.

class SignUp(models.Model):
    firstname = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    password = models.CharField(default='', max_length=15)
    
    def __str__(self):
        return self.firstname

class Expense(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField()
    owner = models.ForeignKey(SignUp, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.item


class ContactForm(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    details = models.CharField(max_length=1000, default='')
    
    def __str__(self):
        return self.name