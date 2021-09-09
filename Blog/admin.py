from django.contrib import admin

# Register your models here.
from .models import Students, Blog, Comment

admin.site.register(Students)
admin.site.register(Blog)
admin.site.register(Comment)
