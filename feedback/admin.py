from django.contrib import admin
from feedback.models import Feedbacks
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):

    list_display = ['name', 'message']

admin.site.register(Feedbacks, FeedbackAdmin)