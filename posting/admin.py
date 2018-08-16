from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Posten, Postko, PostCommenten, PostCommentko, PostTagko, PostTagen

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Posten)
admin.site.register(Postko)
admin.site.register(PostCommenten)
admin.site.register(PostCommentko)
admin.site.register(PostTagko)
admin.site.register(PostTagen)
