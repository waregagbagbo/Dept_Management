from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


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
    email = models.EmailField(_('email_address'), unique =True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    """
    This line specifies that all objects for the class come from the CustomUserManager
    """
    objects = CustomUserManager()   
    
    def __str__(self):
        return "{}".format(self.email)
    
    
class UserProfile(models.Model):
    usre = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}".format(self.usre)
    
    

    
    
    