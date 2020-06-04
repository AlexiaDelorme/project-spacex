from django.contrib import admin
from .models import ContactDetail, Passenger


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'phone_number',
        'country',
    )

    ordering = ('user',)


class PassengerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'birth_date',
        'citizenship',
        'passport_id',
    )

    ordering = ('user',)


# Register your models here.
admin.site.register(ContactDetail, ContactAdmin)
admin.site.register(Passenger, PassengerAdmin)
