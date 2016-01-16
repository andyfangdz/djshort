from django.contrib import admin
from redirect.models import Redirect


# Register your models here.
class RedirectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'last_update')

admin.site.register(Redirect, RedirectAdmin)
