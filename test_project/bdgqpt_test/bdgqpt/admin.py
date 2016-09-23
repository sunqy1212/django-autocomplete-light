from django.contrib import admin
from bdgqpt.models import *
from django.contrib.auth.models import User

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('full_name','ID_No','phone_number')

class CaoZuoPiaoAdmin(admin.ModelAdmin):
    list_display=('nipiaoren',)
# Register your models here.
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(CaoZuoPiao,CaoZuoPiaoAdmin)


