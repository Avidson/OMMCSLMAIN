from django.db import models

# Create your models here.

class Feedbacks(models.Model):
    name = models.CharField(max_length=300, editable=False)
    message = models.TextField(editable=False)

    def __str__(self):
        return self.name 

