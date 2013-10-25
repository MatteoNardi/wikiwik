from django.contrib import admin
from wiki.models import Page, Picture

class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class PictureAdmin(admin.ModelAdmin):
    fields = ['title', 'picture']
    list_display = ('title',)


admin.site.register(Page, PageAdmin)
admin.site.register(Picture, PictureAdmin)
