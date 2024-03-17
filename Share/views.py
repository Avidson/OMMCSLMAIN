from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from custom_code import pass_code as encrypter
from django.db.models import Q 
from django.forms.models import inlineformset_factory
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from Membership.models import Membership_verification

# Create your views here.


@login_required
def share_holding(request, *args, **kwargs):

    try:

        if Membership_verification.objects.filter(client_name=request.user).exists():
            obj = get_object_or_404(Membership_verification, client_name=request.user)
            
            if obj.verification_status == True:
                context = {}
                return render(request, 'shares/shares_index.html', context=context)

            elif obj.verification_status == False:
                return HttpResponseRedirect('/Membership/pending/') 
            else:
                return HttpResponseRedirect('/verification-required/')

    except SystemError as e:
        print('Error at'.format(e))
        
    context = {

    }

    return render(request, 'shares/shares_index.html', context=context)

@login_required
def send_payment_for_share(request, *args, **kwargs):

    context = {

    }

    return render(request, 'shares/shares_send_payment.html', context=context)


@login_required
def withdrawal_request(request, *args, **kwargs):
    
    context = {

    }

    return render(request, 'shares/withdrawal.html', context=context)

@login_required
def shares_detail_view(request, *args, **kwargs):
    
    context = {

    }

    return render(request, 'shares/shares_detail.html', context=context)



