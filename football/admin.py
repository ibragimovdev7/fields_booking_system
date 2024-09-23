from django.contrib import admin
from .models import FootballField, FieldImage

class FieldImageInline(admin.TabularInline):
    model = FieldImage
    extra = 4

class FootballFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'price_per_hour')
    list_filter = ('price_per_hour',)
    search_fields = ('name', 'address')
    inlines = [FieldImageInline]

admin.site.register(FootballField, FootballFieldAdmin)
admin.site.register(FieldImage)
