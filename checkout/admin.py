from django.contrib import admin
from .models import OtherPassenger, BookingReference


class OtherPassengerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birth_date',
        'citizenship',
        'passport_id',
    )

    ordering = ('last_name',)


class BookingReferenceAdmin(admin.ModelAdmin):
    list_display = (
        'trip',
        'booker',
        'confirmation_status',
    )

    ordering = ('trip',)


# Register your models here.
admin.site.register(OtherPassenger, OtherPassengerAdmin)
admin.site.register(BookingReference, BookingReferenceAdmin)
