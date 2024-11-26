# from django.contrib import admin
# from .models import related models
from django.contrib import admin
from .models import CarMake, CarModel

# Inline class for CarModel
class CarModelInline(admin.TabularInline):  # Use StackedInline if you prefer a stacked layout
    model = CarModel
    extra = 1  # Number of empty rows to display for adding new models
    fields = ('name', 'type', 'year', 'dealer_id')  # Fields to show in the inline admin
    show_change_link = True  # Add a link to edit the related CarModel entry

# Register the CarMake model with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'established')
    search_fields = ('name',)
    list_filter = ('established',)
    inlines = [CarModelInline]  # Attach the inline

# Register the CarModel model with customizations
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    search_fields = ('name', 'car_make__name')
    list_filter = ('type', 'year', 'car_make')
    ordering = ('year',)
    raw_id_fields = ('car_make',)
    list_per_page = 20

# Register models to the admin site
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)