from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1
    fields = ('name', 'type', 'year', 'dealer_id')
    show_change_link = True


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'established')
    search_fields = ('name',)
    list_filter = ('established',)
    inlines = [CarModelInline]


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    search_fields = ('name', 'car_make__name')
    list_filter = ('type', 'year', 'car_make')
    ordering = ('year',)
    raw_id_fields = ('car_make',)
    list_per_page = 20


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
