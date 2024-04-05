from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    """_summary_
    create a class that subclassess AbstractUser
    Removed username field
    made the email field required and unique
    Args:
        AbstractUser (_type_): _description_
    """
    username = None
    email = models.EmailField(_('email_address'), unique =True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    """
    This line specifies that all objects for the class come from the CustomUserManager
    """
    objects = CustomUserManager
    
    
    def __str__(self):
        return self.email
    