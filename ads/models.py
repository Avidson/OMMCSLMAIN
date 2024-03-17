from django.db import models

# Create your models here.

class Display_ads(models.Model):
    ads_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/')
    organisation_name = models.CharField(max_length=200)
    ads_url = models.CharField(max_length=300, default=None)
    ads_starts = models.DateTimeField()
    ads_end = models.DateTimeField() 

    def __str__(self):
        return self.organisation_name 
