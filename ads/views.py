from django.shortcuts import render
from ads.models import Display_ads
# Create your views here.



def ads_view(request, *args, **kwargs):
    

    context = {

    }

    return render(request, '', context=context)