from django.contrib import admin
from .models import Car, ContactMessage, UserProfile


# Custom displays within Django admin

class CarAdmin(admin.ModelAdmin):
    list_display    = ('vehicleId',
                       'make',
                       'trim',
                       'yearIntroduced',
                       'currentlyAvailable'
                       )

    # Search Field in Django Admin
    search_fields   = ('vehicleId',
                       'make',
                       'trim'
                       )

# Registration of sites

admin.site.register(UserProfile)
admin.site.register(Car, CarAdmin)
admin.site.register(ContactMessage)


