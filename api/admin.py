from django.contrib import admin

from .models import Interview, Subject, Temp_subj, Template

# Register your models here.
admin.site.register(Subject)
admin.site.register(Interview)
admin.site.register(Temp_subj)
admin.site.register(Template)

