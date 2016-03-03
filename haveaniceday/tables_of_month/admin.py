from django.contrib import admin
from .models import TableOfMonth, Shift

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

#@admin.register(Shift)
#class ShiftAdmin(admin.ModelAdmin):
#    list_display = ['date', 'man', 'substitute', 'table']
