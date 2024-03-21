from django.contrib import admin
from users.models import User
from appointments.admin import RecordsAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (RecordsAdmin,)