from django.db import models

# Create your models here.


class Create_Branch(models.Model):
    branch_name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    creator = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.creator
