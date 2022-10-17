from django.contrib import admin

from .models import CustomUser,TeamCatagory,Team

admin.site.register(CustomUser)
admin.site.register(TeamCatagory)
admin.site.register(Team)

# Register your models here.
