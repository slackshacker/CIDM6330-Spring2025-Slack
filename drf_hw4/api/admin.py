
# ViewSets – Django REST Framework: https://www.django-rest-framework.org/api-guide/viewsets/

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Applicant, Contact, Address

# Register models for Django Admin
admin.site.register(Applicant)
admin.site.register(Contact)
admin.site.register(Address)
