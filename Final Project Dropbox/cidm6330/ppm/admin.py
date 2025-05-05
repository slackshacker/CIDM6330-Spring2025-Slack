from django.contrib import admin

# Register your models here.
from .models import Applicant, Address, Contact

# Register my models to show them in Django Admin.
admin.site.register(Applicant)
admin.site.register(Address)
admin.site.register(Contact)
