from django.contrib import admin
from .models import Artical

class ArticalAdmin(admin.ModelAdmin):
    list_display=('title','content')

admin.site.register(Artical)
