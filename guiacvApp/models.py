from django.db import models
from datetime import datetime
# Create your models here.


class form_register(models.Model):
    class Meta:
        verbose_name_plural = 'form register'

    Name = models.CharField(max_length=200)
    Telephone1 = models.CharField(max_length=200)
    Telephone2 = models.CharField(max_length=200)
    Celular = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Website = models.TextField()
    Address = models.TextField()
    City = models.CharField(max_length=200)
    Island = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)
    Sub_Category = models.CharField(max_length=200)
    Description = models.TextField()
    Photo1 = models.ImageField(upload_to='uploads/Photo1/')
    Photo2 = models.ImageField(upload_to='uploads/Photo2/', null=True, blank=True, default='')
    Photo3 = models.ImageField(upload_to='uploads/Photo3/', null=True, blank=True, default='')
    Photo4 = models.ImageField(upload_to='uploads/Photo4/', null=True, blank=True, default='')
    time = models.DateField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.Name

