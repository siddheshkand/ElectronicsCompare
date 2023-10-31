from django.contrib import admin
from mobile.models import Mobile
# Register your models here.


class MobileAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description')

admin.site.register(Mobile, MobileAdmin)