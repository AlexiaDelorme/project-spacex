from django.contrib import admin
from . import models


class DepartureSiteAdmin(admin.ModelAdmin):
    list_display = (
        'site_name',
        'country',
        'site_code'
    )

    ordering = ('country',)


class TripCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'destination',
        'price',
        'destination_code'
    )

    ordering = ('destination',)


class TripAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'departure_date',
        'return_date',
        'slot',
    )

    ordering = ('departure_date',)


# Register your models here.
admin.site.register(models.DepartureSite, DepartureSiteAdmin)
admin.site.register(models.RequiredDocument)
admin.site.register(models.TripImage)
admin.site.register(models.TripCategory, TripCategoryAdmin)
admin.site.register(models.Trip, TripAdmin)
