from django.contrib import admin
from .models import ContactDetail, Passenger

# Register your models here.
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


admin.site.register(ContactDetail, ContactAdmin)
admin.site.register(Passenger, PassengerAdmin)