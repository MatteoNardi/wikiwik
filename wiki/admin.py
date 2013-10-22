from django.contrib import admin
from wiki.models import Page

class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Page, PageAdmin)
