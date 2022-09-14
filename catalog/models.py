from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True,  
        help_text='Category Name'
    )
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self):
        self.name = self.name.upper()
        super(Category, self).save()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True,  
        help_text='Service Name'
    )
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Services'

    def save(self):
        self.name = self.name.upper()
        super(Service, self).save()

    def __str__(self):
        return self.name