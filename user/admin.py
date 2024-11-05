from django.contrib import admin

# Register your models here.

from .models import Custom_User

admin.site.register(Custom_User)