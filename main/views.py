from django.shortcuts import render, redirect, get_object_or_404
from .models import Message, Profile
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from custom_code import pass_code as encrypter
from django.db.models import Q
from django.forms.models import inlineformset_factory
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.conf import settings
import requests
import json
import weasyprint
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from Membership.models import Membership_verification
from .tasks import payment_completed
from inAppDonations.models import InAppDonations
from Share.models import Payment_for_Share
from Loan_Request.models import  loan_request_list 
from Monthly_due.models import (
    January,
    February,
    March,
    April,
    May,
    June,
    July,
    August,
    September,
    October,
    November,
    December
)
from django.db.models import Sum
# Create your views here.

api_key = settings.PAYSTACK_SECRETE_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL

#The below code cover almost every component found on the app's index page.
def index_page(request, *args, **kwargs):

    form = User(request.POST)

    if request.method == 'POST':
        username = request.POST['username']
        passcode = request.POST['passcode']
        user = auth.authenticate(username=username, password=passcode)

        try:
            if user is not None:
                auth.login(request, user)
                #Calling the Profile objects to verify paid status
                """ The section of the code below take in the parament of checking
                if a registered member has made a successful payment. if the payment was
                sucessful, member will have access to dashboard for other operation, else
                member will be limited to the payment gateway."""

                if Profile.objects.filter(profile_owner=request.user).exists():
                    check_membership_paid_status = get_object_or_404(Profile,
                    profile_owner = request.user)

                    if check_membership_paid_status.paid == True:
                        return redirect('main:dashboard')

                    elif check_membership_paid_status.paid == False:
                        if Profile.objects.filter(profile_owner=request.user).exists():
                            return redirect('main:processing-payment')
                    else:
                    #request.session['registration_id'] = check_membership_paid_status.id
                        return redirect(reverse('main:registration-fee'))
                else:
                    return redirect(reverse('main:registration-fee'))

        except ObjectDoesNotExist():
            return redirect('/')

        else:
            messages.info(request, "Your pin didn't match the ones in our system")
            return redirect('/')

    context = {
        'form' : form,
    }
    return render(request, 'index.html', context=context)


#This view if for projects about page, any changes on about should be found here
#This view if for projects about page, any changes on about should be found here
def about_page(request, *args, **kwargs):
    return render(request, 'about.html', {})


#This view is for project's contact page, any changes on service should be found here
#This view is for project's contact page, any changes on service should be found here
def contact_page(request, *args, **kwargs):

    form = Message(request.POST)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        new_message = Message.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )

        if new_message:
            return redirect('Membership:success')

    return render(request, 'contact.html', {})


#This view is for project's service page, any changes on service should be found here
#This view is for project's service page, any changes on service should be found here
def services_page(request, *args, **kwargs):
    return render(request, 'services.html', {})


@login_required
def Dashboard(request, *args, **kwargs):


    try:
        if Membership_verification.objects.filter(client_name=request.user).exists():
            #To apply check paramenter for all verified users
            verified_tag = get_object_or_404(Membership_verification, client_name=request.user)      
       
            user = request.user
            total_amount_donations = InAppDonations.objects.filter(client_name=user, paid=True).aggregate(Sum('amount'))['amount__sum'] or 0
            total_loan_approved = loan_request_list.objects.filter(client_name=user, loan_approval=True).aggregate(Sum('loan_amount'))['loan_amount__sum'] or 0
            total_loan_approved_emi = loan_request_list.objects.filter(client_name=user, loan_approval=True).aggregate(Sum('emi'))['emi__sum'] or 0
            context ={
                'total_amount_donations' : total_amount_donations,
                'total_loan_approved' : total_loan_approved,
                'verified_tag' : verified_tag,
                'total_loan_approved_emi': total_loan_approved_emi
            }
            return render(request, 'dashboard.html', context=context)     
        
    except ObjectDoesNotExist:
        pass

    except SystemError as e:
        import sys
        sys.exit('Error {} captured'.format(e))
    
    context = {}
    return render(request, 'dashboard.html', context=context)

           

def logout(request, *args, **kwargs):
    auth.logout(request)
    return redirect('/')


@login_required
def ProfileEdit(request):
    try:
        if request.method == 'POST' and request.FILES:

            occupation = request.POST['occupation']
            state_residence = request.POST['state-of-residence']
            home_address = request.POST['home-address']
            phone_number = request.POST['phone-number']
            passport = request.FILES['passport']

            fs = FileSystemStorage()
            filename = fs.save(passport.name, passport)
            upload_media = fs.url(filename)

            profile = Profile.objects.get_or_create(
                profile_owner = request.user,
                occupation = occupation,
                state_residence = state_residence,
                home_address = home_address,
                phone_number = phone_number,
                passport = passport,
            )

            if profile:
                return redirect (reverse('main:registration-fee'))

    except ObjectDoesNotExist:
        print('Object Not Available')

    context = {

        }

    return render(request, 'profile/edit-profile.html', context=context)


""" Redirect view to pay for regitration """
@login_required
def registration_fee_payment(request):

    try:
        if request.user is not None:
            if request.method == 'POST' and request.FILES:
                registration_fee_payment = request.POST['amount']
                first_name = request.POST['first-name']
                last_name = request.POST['last-name']
                email = request.POST['email']
                occupation = request.POST['occupation']
                state_residence = request.POST['state-of-residence']
                home_address = request.POST['home-address']
                phone_number = request.POST['phone-number']
                passport = request.FILES['passport']

                #handles the uploading of image file
                fs = FileSystemStorage()
                filename = fs.save(passport.name, passport)
                upload_media = fs.url(filename)


                registration_payment, created = Profile.objects.get_or_create(
                    profile_owner = request.user,
                    registration_fee = registration_fee_payment,
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    occupation = occupation,
                    state_residence = state_residence,
                    home_address = home_address,
                    phone_number = phone_number,
                    passport = passport,
                )
                if registration_payment:
                    return redirect(reverse('main:processing-payment'))

    except ObjectDoesNotExist:
        pass

    context = {

    }
    return render(request, 'main/registration_fee_payment.html', context=context)


#registration payment portal
@login_required
def payment_process(request):

    payment_id = request.session.get('registration_id')
    payment = get_object_or_404(Profile, profile_owner=request.user)
    amount = payment.get_registration_fee() * 100

    if request.method == 'POST':


        success_url = request.build_absolute_uri(
            reverse('main:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('main:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'email' : payment.email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            print('Test pass!')
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass
        else:
            return render(request, 'main/process_payment.html', locals())

    else:
        return render(request, 'main/process_payment.html', locals())


@login_required
def payment_success(request):

    # retrive the payment_id we'd set in the django session ealier
    payment_id = request.session.get('registration_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(Profile, profile_owner=request.user,)#new

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
    if res_['status'] == 'success':  # new
        # update payment payment reference
        if payment:
            payment.paid = True
            payment.payment_ref = ref #new
            payment.save()#new

            #launch asynchronous task to send mail
            payment_completed.delay(payment.pk)
        else:
            pass

    return render(request, 'main/payment_success.html', {'res':res})
    
@login_required
def payment_canceled(request):
    return render(request, 'main/payment_cancel.html', {})



@staff_member_required
def payment_pdf_generator(request, pk):
    your_invoice = 'your_invoice'
    payment = get_object_or_404(Profile, pk=pk)
    html = render_to_string('main/pdf.html', {'payment': payment})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename={your_invoice}-{payment.payment_date}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + 'assets/css/main.css'
        )])
    return response




@login_required
def generate_account_statement(request, *args, **kwargs):
    
    inappdonation_transactions = InAppDonations.objects.filter(client_name=request.user, paid=True).order_by('-timestamp')
    loan_request_transactions = loan_request_list.objects.filter(client_name=request.user, loan_approval=True).order_by('-timestamp')
    shares_transactions = Payment_for_Share.objects.filter(client_name=request.user, paid=True).order_by('-timestamp')

    total_amount_donations = InAppDonations.objects.filter(client_name=request.user, paid=True).aggregate(Sum('amount'))['amount__sum'] or 0
    total_amount_loanrequest = loan_request_list.objects.filter(client_name=request.user, loan_approval=True).aggregate(Sum('loan_amount'))['loan_amount__sum'] or 0
    total_amount_shares = Payment_for_Share.objects.filter(client_name=request.user, paid=True).aggregate(Sum('amount'))['amount__sum'] or 0

    overall_total = total_amount_donations + total_amount_loanrequest + total_amount_shares

    context = {
            'inappdonation_transactions' : inappdonation_transactions,
            'loan_request_transactions' : loan_request_transactions,
            'shares_transactions' : shares_transactions,
            'overall_total' : overall_total
    }

    return render(request, 'statement.html', context=context)


def account_statement_generate_pdf(request, *args, **kwargs):

    inappdonation_transactions = InAppDonations.objects.filter(client_name=request.user, paid=True).order_by('-timestamp')
    loan_request_transactions = loan_request_list.objects.filter(client_name=request.user, loan_approval=True).order_by('-timestamp')
    shares_transactions = Payment_for_Share.objects.filter(client_name=request.user, paid=True).order_by('-timestamp')

    total_amount_donations = InAppDonations.objects.filter(client_name=request.user, paid=True).aggregate(Sum('amount'))['amount__sum'] or 0
    total_amount_loanrequest = loan_request_list.objects.filter(client_name=request.user, loan_approval=True).aggregate(Sum('loan_amount'))['loan_amount__sum'] or 0
    total_amount_shares = Payment_for_Share.objects.filter(client_name=request.user, paid=True).aggregate(Sum('amount'))['amount__sum'] or 0

    overall_total = total_amount_donations + total_amount_loanrequest + total_amount_shares
    context={
        'inappdonation_transactions' : inappdonation_transactions,
        'loan_request_transactions' : loan_request_transactions,
        'shares_transactions' :  shares_transactions,
        'overall_total' : overall_total
    }

    your_account_statement = 'OMMCSL - Account Statement'
    html = render_to_string('statement.html', context=context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename={your_account_statement}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + 'assets/css/passcode.css'
        )])

    return response
