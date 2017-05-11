from django.db import models
from django.core.urlresolvers import reverse

# Creating Model For Contact Form


class Contact(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=10000)

    def get_absolute_url(self):
        return reverse('contact:index')

    def __str__(self):
        return self.firstName
