from django.contrib import admin
from . models import *
# Register your models here.


class Monthly_dueAdminSite(admin.AdminSite):
    def get_app_list(self, request):

        ordering = {
            'Januarys' : 1,
            'Februarys' : 2,
            'Marchs': 3,
            'Aprils' : 4,
            'Mays': 5,
            'Junes': 6,
            'Julys' : 7,
            'Augusts': 8,
            'Septembers':9,
            'Octobers' : 10,
            'Novembers' : 11,
            'Decembers' : 12,
        }
    
        app_dict = self._build_app_dict(request)

        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        for app in app_list:
            app['name'].sort(key=lambda x: ordering[x['name']])
        
        return app_list


class JanuaryAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
    class Meta:
        Monthly_dueAdminSite
admin.site.register(January, JanuaryAdmin)


class FebruaryAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(February, FebruaryAdmin)

class MarchAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(March, MarchAdmin)

class AprilAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(April, AprilAdmin)

class MayAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(May, MayAdmin)

class JuneAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(June, JuneAdmin)

class JulyAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(July, JulyAdmin)

class AugustAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(August, AugustAdmin)

class SeptemberAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(September, SeptemberAdmin)

class OctoberAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(October, OctoberAdmin)

class NovemberAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(November, NovemberAdmin)

class DecemberAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
admin.site.register(December, DecemberAdmin)

