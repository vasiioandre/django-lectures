from django.contrib import admin
from cars.models import Car

# Register your models here.
# admin.site.register(Car)


class CarAdmin(admin.ModelAdmin):
    # reverse the order of the fields
    # fields = ['year', 'brand']
    # split the fileds into field sets
    fieldsets = [
        ('TIME INFORMATION', {'fields': ['year']}),
        ('CAR INFORMATION', {'fields': ['brand']})
    ]


admin.site.register(Car, CarAdmin)
