from django.contrib import admin
from .models import Tovar, NotifyForAdmin


class TovarsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'available', 'created']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Tovar, TovarsAdmin)


class NotifyAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created']
    list_filter = ['created', 'title']
admin.site.register(NotifyForAdmin, NotifyAdmin)
