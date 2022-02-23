from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

admin.site.site_header = 'Proyecto con Django'
admin.site.site_title = 'Proyecto con Django'
admin.site.index_title = 'Panel de Gestion'
