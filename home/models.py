
from django.db import models

# Create your models here.
class Contact(models.Model):
      name = models.CharField(max_length=122)
      email = models.CharField(max_length=122)
      phone = models.CharField(max_length=12)
      desc = models.TextField()
      date = models.DateField()
      def __str__(self):
            return self.name


class UaeTicket(models.Model):
      name = models.CharField(max_length=122, null=False)
      email = models.CharField(max_length=122, null=False)
      cnic = models.CharField(max_length=12, null=False)
      passport = models.CharField(max_length=1243, null=False)
      payment = models.CharField(max_length=1243, null=False)
      account = models.CharField(max_length=1243, null=False)
      place = models.CharField(max_length=1243, null=False)
      image = models.ImageField(default='')
      date = models.DateField()
      def __str__(self):
            return self.name

class hotels(models.Model):
      name = models.CharField(max_length=122, null=False)
      email = models.CharField(max_length=122, null=False)
      account = models.CharField(max_length=12, null=False)
      payment = models.CharField(max_length=12, null=False)
      date = models.DateField()
      def __str__(self):
            return self.name


class Signup(models.Model):
      fname = models.CharField(max_length=122, null=False)
      lname = models.CharField(max_length=122, null=False)
      email = models.CharField(max_length=12, null=False)
      pass1 = models.CharField(max_length=12, null=False)
      pass2 = models.CharField(max_length=12, null=False)
      def __str__(self):
            return self.name




