from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['email']
    # prepopulated_fields = {'slug': ('name',)}

