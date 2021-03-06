from django.contrib import admin
from .models import *

class CarAdmin(admin.ModelAdmin):
    fields = ["name", "brand", "year", "country", "car_id"]
    class Meta:
        model = Car

admin.site.register(Car, CarAdmin)

class ModelTabularInline(admin.TabularInline):
    model = Model
    extra = 0
    fields = ['name', 'alias', 'min_price', 'max_price']

class MakeAdmin(admin.ModelAdmin):
    inlines = [ModelTabularInline]
    class Meta:
        model = Make

class YearFilterTabularInline(admin.TabularInline):
    model = YearFilter
    extra = 0
    fields = ['from_year', 'to_year']

class PriceFilterTabularInline(admin.TabularInline):
    model = Price
    extra = 0
    fields = ['year', 'usa_low_price', 'usa_avg_price', 'usa_high_price', 'uk_low_price', 'uk_avg_price', 'uk_high_price']    

class ModelAdmin(admin.ModelAdmin):
    inlines = [YearFilterTabularInline, PriceFilterTabularInline]
    class Meta:
        model = Model

admin.site.register(Make, MakeAdmin)
admin.site.register(Model, ModelAdmin)

class BlockAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('car_id', )

admin.site.register(Block, BlockAdmin)

