from django.contrib import admin
from .models import TableOfMonth, Shift
from website_component.models import CustomWebPage, CustomComponent

# Register your models here.

class ShiftInline(admin.TabularInline):
    model = Shift
    extra = 1

@admin.register(TableOfMonth)
class TableOfMonthAdmin(admin.ModelAdmin):
    list_display = ['table_view', 'author', 'confirm', 'date', 'notes']
    inlines = [ShiftInline]

    def table_view(self, obj):
        return obj

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['date', 'man', 'substitute', 'table']

class CustomComponentInline(admin.TabularInline):
    model = CustomComponent
    extra = 1

@admin.register(CustomWebPage)
class CustomWebPageAdmin(admin.ModelAdmin):
    list_display = ['page_view']
    inlines = [CustomComponentInline]

    def page_view(self, obj):
        return obj

@admin.register(CustomComponent)
class CustomComponentAdmin(admin.ModelAdmin):
    list_display = ['name']

# Website_component

#@admin.register(Shift)
#class ShiftAdmin(admin.ModelAdmin):
#    list_display = ['date', 'man', 'substitute', 'table']
