from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """_summary_
    
    Custom user model manager where email is the unique identifier for authentication instead of username

    Args:
        BaseUserManager (_type_): _description_
    """
    def create_user(self, email,password, **extra_fields):
        """_summary_
        create and save a user with email and password

        Args:
            email (_type_): _description_
            pasword (_type_): _description_
        """
        if not email:
            raise ValueError(_("The email must be set"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, password, **extra_fields):
        """_summary_

        Args:
            email (_type_): _description_
            password (_type_): _description_
        """
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True),
        extra_fields.setdefault("is_active",True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser = True"))
        
        return self.create_user(email, password, **extra_fields)