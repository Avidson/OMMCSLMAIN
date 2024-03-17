from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from Monthly_due import views





app_name = 'Monthly_due'

urlpatterns = [
    path('', views.month_indexview, name='home_monthly'),
    path('january/', views.january_due, name='january_due'),
    path('february/', views.february_due, name='february_due'),
    path('march/', views.march_due, name='march_due'),
    path('april/', views.april_due, name='april_due'),
    path('may/', views.may_due, name='may_due'),
    path('june/', views.june_due, name='june_due'),
    path('july/', views.july_due, name='july_due'),
    path('august/', views.august_due, name='august_due'),
    path('september/', views.september_due, name='september_due'),
    path('october/', views.october_due, name='october_due'),
    path('november/', views.november_due, name='november_due'),
    path('december/', views.december_due, name='december_due'),
    path('payment-process/', views.payment_process_jan, name='payment-process'),
    path('payment-success/', views.payment_success_jan, name='payment-success'),
    path('payment-process/', views.payment_process_feb, name='payment-process'),
    path('payment-success/', views.payment_success_feb, name='payment-success'),
    path('payment-process/', views.payment_process_mar, name='payment-process'),
    path('payment-success/', views.payment_success_mar, name='payment-success'),
    path('payment-process/', views.payment_process_apr, name='payment-process'),
    path('payment-success/', views.payment_success_apr, name='payment-success'),
    path('payment-process/', views.payment_process_may, name='payment-process'),
    path('payment-success/', views.payment_success_may, name='payment-success'),
    path('payment-process/', views.payment_process_jun, name='payment-process'),
    path('payment-success/', views.payment_success_jun, name='payment-success'),
    path('payment-process/', views.payment_process_jul, name='payment-process'),
    path('payment-success/', views.payment_success_jul, name='payment-success'),
    path('payment-process/', views.payment_process_aug, name='payment-process'),
    path('payment-success/', views.payment_success_aug, name='payment-success'),
    path('payment-process/', views.payment_process_sep, name='payment-process'),
    path('payment-success/', views.payment_success_sep, name='payment-success'),
    path('payment-process/', views.payment_process_oct, name='payment-process'),
    path('payment-success/', views.payment_success_oct, name='payment-success'),
    path('payment-process/', views.payment_process_nov, name='payment-process'),
    path('payment-success/', views.payment_success_nov, name='payment-success'),
    path('payment-process/', views.payment_process_dec, name='payment-process'),
    path('payment-success/', views.payment_success_dec, name='payment-success'),
    path('payment-canceled/', views.payment_canceled, name='payment-canceled'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)