from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Model_Event



# admin.site.register(Model_Event, Model_EventAdmin)
admin.site.register(Model_Event)
