from django.contrib import admin
from django.contrib.auth.models import User
from parkpedia.models import Park, FavouritePark
from django.shortcuts import render_to_response, redirect, render
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PATH = os.path.join(BASE_DIR, 'load_data.py')


# Register your models here.
class ImportAdmin(admin.ModelAdmin):
    actions = ['load_data']

    def load_data(self, request, queryset):
        execfile(PATH)

    load_data.short_description = "Import data"


class FavouriteParkAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['initial'] = request.user.id
        return super(FavouriteParkAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

admin.site.register(Park, ImportAdmin)
admin.site.register(FavouritePark, FavouriteParkAdmin)
