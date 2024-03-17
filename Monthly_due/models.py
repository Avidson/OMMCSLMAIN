from django.db import models
from django.conf import settings
from main.models import Profile

# Create your models here.


class January(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class February(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class March(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class April(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class May(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class June(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class July(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class August(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class September(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class October(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class November(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

class December(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

    
 