from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("isim","email")
    list_filter = ("mesaj",)
    search_fields = ("mesaj",)