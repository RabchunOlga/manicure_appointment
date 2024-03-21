from django.contrib import admin
from appointments.models import AppointmentCategory, AppointmentsListModel, Records

admin.site.register(AppointmentCategory)


@admin.register(AppointmentsListModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    fields = ('image', 'name', 'description', 'price', 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


class RecordsAdmin(admin.TabularInline):
    model = Records
    fields = ('appointment', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
