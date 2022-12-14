
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager , PermissionsMixin

# AUTH_USER_MODEL = 'user.CustomUser'

class CustomUserManager(BaseUserManager):

    def create_user(self,email, password = None , **extra_fields):
        if not email:
            raise ValueError("You have not porvided valid emil address")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)    
        extra_fields.setdefault('is_superuser', True)    
        return self.create_user(email,password, **extra_fields)  


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200, unique = True,)
    username = models.CharField(max_length = 255 , unique = True)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff  = models.BooleanField(default=False)

    carated_at = models.DateTimeField(auto_now_add = True)
    last_logedin = models.DateTimeField(auto_now = True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

    def get_short_name(self):
        return self.email  

    def has_perm(self, perm , obj=None):
        return self.is_superuser

    def has_module_perms(self, app_lebel):
        return self.is_superuser

    class Meta:
        verbose_name_plural = 'Users'



class TeamCatagory(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self) -> str:
        return self.name



class Team(models.Model): 
    name = models.OneToOneField(TeamCatagory, on_delete = models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'client')
    member = models.ManyToManyField(CustomUser)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self) -> str:
        return self.name.name 

















