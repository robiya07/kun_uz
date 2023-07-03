from django.contrib import admin

from main.models import ZoneModel, NewsModel, TagModel, CategoryModel

# Register your models here.
admin.site.register(ZoneModel)
admin.site.register(NewsModel)
admin.site.register(CategoryModel)
admin.site.register(TagModel)
