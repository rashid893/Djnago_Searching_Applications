from django.contrib import admin

# Register your models here.
from home.models import Employclass,Companyclass
admin.site.register(Employclass)
admin.site.register(Companyclass)