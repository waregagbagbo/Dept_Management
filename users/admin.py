from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms  import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser, UserProfile

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email','is_staff','is_active',)
    fieldsets = ((None, {"fields": ("email", "password")}),("permissions",{"fields": ("is_staff","is_active", "groups", "user_permissions")}),)
    
    add_fieldsets =(
        (None, {
            "classes":("wide"),
            "fields":(
                "email","password1","password2", "is_staff",
                "is_active","groups","user_permissions"
            )
        }),
    )
    
    search_fields = ('email',)
    ordering =("email",)
    
    
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete=False
    verbose_plural_name="User Profile"
    fk_name = 'user' 
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)