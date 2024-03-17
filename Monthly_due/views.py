from django.shortcuts import render
from .models import *
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
import json
from main.models import Profile
# Create your views here.

#PAYMENT GATEWAY API CREDENTIALS
api_key = settings.PAYSTACK_SECRETE_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL


@login_required
def january_due(request, *args, **kwargs):

    form = January(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            january_payment, created = January.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if january_payment:
                request.session["january_payment_session_id"] = january_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/january.html', context=context)

@login_required
def february_due(request, *args, **kwargs):
    form = February(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            february_payment, created = February.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if february_payment:
                request.session["february_payment_session_id"] = february_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass
    context={}
    return render(request, 'monthly_due/february.html', context=context)

@login_required
def march_due(request, *args, **kwargs):
    form = March(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            march_payment, created = March.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if march_payment:
                request.session["march_payment_session_id"] = march_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/march.html', context=context)

@login_required
def april_due(request, *args, **kwargs):
    form = April(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            april_payment, created = April.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if april_payment:
                request.session["april_payment_session_id"] = april_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/april.html', context=context)

@login_required
def may_due(request, *args, **kwargs):
    form = May(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            may_payment, created = May.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if may_payment:
                request.session["may_payment_session_id"] = may_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/may.html', context=context)

@login_required
def june_due(request, *args, **kwargs):
    form = June(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            june_payment, created = June.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if june_payment:
                request.session["june_payment_session_id"] = june_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/june.html', context=context)

@login_required
def july_due(request, *args, **kwargs):
    form = July(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            july_payment, created = July.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if july_payment:
                request.session["july_payment_session_id"] = july_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/july.html', context=context)

@login_required
def august_due(request, *args, **kwargs):
    form = August(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            august_payment, created = August.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if august_payment:
                request.session["august_payment_session_id"] = august_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/august.html', context=context)

@login_required
def september_due(request, *args, **kwargs):
    form = September(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            september_payment, created = September.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if september_payment:
                request.session["september_payment_session_id"] = september_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/september.html', context=context)

@login_required
def october_due(request, *args, **kwargs):
    form = October(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            october_payment, created = October.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if october_payment:
                request.session["october_payment_session_id"] = october_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/october.html', context=context)

@login_required
def november_due(request, *args, **kwargs):
    form = November(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            november_payment, created = November.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if november_payment:
                request.session["november_payment_session_id"] = november_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/november.html', context=context)

@login_required
def december_due(request, *args, **kwargs):
    form = December(request.POST)
    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            december_payment, created = December.objects.get_or_create( 
                client_name = request.user,
                amount = amount
                 )

            if december_payment:
                request.session["december_payment_session_id"] = december_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass

    context = {}
    return render(request, 'monthly_due/december.html', context=context)

@login_required
def month_indexview(request):
    context = {}
    return render(request, 'monthly_due/home.html', context=context)


#January payment session
@login_required
def payment_process_jan(request):

    payment_id = request.session.get('january_payment_session_id')
    payment = get_object_or_404(January, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


@login_required
def payment_success_jan(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('january_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(January, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})


#February payment session
@login_required
def payment_process_feb(request):

    payment_id = request.session.get('february_payment_session_id')
    payment = get_object_or_404(February, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


@login_required
def payment_success_feb(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('february_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(February, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})



#March payment session
@login_required
def payment_process_mar(request):

    payment_id = request.session.get('march_payment_session_id')
    payment = get_object_or_404(March, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


@login_required
def payment_success_mar(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('march_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(March, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})


#April payment session
@login_required
def payment_process_apr(request):

    payment_id = request.session.get('april_payment_session_id')
    payment = get_object_or_404(April, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


@login_required
def payment_success_apr(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('april_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(April, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})

#April payment session
@login_required
def payment_process_may(request):

    payment_id = request.session.get('may_payment_session_id')
    payment = get_object_or_404(May, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


#May payment session
@login_required
def payment_success_may(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('may_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(May, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})


#June payment session
@login_required
def payment_process_jun(request):

    payment_id = request.session.get('june_payment_session_id')
    payment = get_object_or_404(June, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


#June payment session
@login_required
def payment_success_jun(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('june_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(June, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})


#July payment session
@login_required
def payment_process_jul(request):

    payment_id = request.session.get('july_payment_session_id')
    payment = get_object_or_404(July, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


#July payment session
@login_required
def payment_success_jul(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('july_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(July, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})


#August payment session
@login_required
def payment_process_aug(request):

    payment_id = request.session.get('august_payment_session_id')
    payment = get_object_or_404(August, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


#August payment session
@login_required
def payment_success_aug(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('august_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(August, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})


#September payment session
@login_required
def payment_process_sep(request):

    payment_id = request.session.get('september_payment_session_id')
    payment = get_object_or_404(September, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


#September payment session
@login_required
def payment_success_sep(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('september_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(September, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})



#October payment session
@login_required
def payment_process_oct(request):

    payment_id = request.session.get('october_payment_session_id')
    payment = get_object_or_404(October, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


#October payment session
@login_required
def payment_success_oct(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('october_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(October, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})



#November payment session
@login_required
def payment_process_nov(request):

    payment_id = request.session.get('november_payment_session_id')
    payment = get_object_or_404(November, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


#November payment session
@login_required
def payment_success_nov(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('november_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(November, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})



#December payment session
@login_required
def payment_process_dec(request):

    payment_id = request.session.get('december_payment_session_id')
    payment = get_object_or_404(December, id=payment_id)
    amount = payment.amount * 100
    profile_email = get_object_or_404(Profile, profile_owner=request.user)
        

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'profile_email' : profile_email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


#December payment session
@login_required
def payment_success_dec(request):
    # retrive the payment_id we'd set 
    payment_id = request.session.get('december_payment_session_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(December, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

  
    return render(request, 'monthly_due/payment_success.html', {})



@login_required
def payment_canceled(request):
    return render(request, 'monthly_due/payment_cancel.html', {})

