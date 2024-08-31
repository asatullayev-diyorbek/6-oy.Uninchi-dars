from django.contrib import admin
from . import models


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'price', 'description')
    list_display_links = ['id', 'title']


admin.site.register(models.Book, BookAdmin)
