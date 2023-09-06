# from django.db import models
# from .AbstractModel import BaseUser

# class User(BaseUser):
#     username = models.CharField(max_length=150, unique=False)
#     first_name = models.CharField(max_length=50, null=True)
#     last_name = models.CharField(max_length=50, null=True)
#     date_birth = models.DateField(null=True)
#     mobile_phone = models.CharField(max_length=14, null=True)
#     street_address = models.CharField(max_length=50, null=True)
#     postal_code = models.CharField(max_length=45, null=True)
#     city = models.CharField(max_length=60, null=True)
#     country = models.CharField(max_length=60, null=True)
#     Favourite_national_team = models.CharField(max_length=50, null=True)
#     Favourite_city = models.CharField(max_length=60, null=True)
#     favourite_language = models.CharField(max_length=60, null=True)
#     club_coeur = models.CharField(max_length=60, null=True)
#     sexe_user = models.CharField(max_length=50, null=True)
#     password_user = models.CharField(max_length=90, null=True)
#     card_number = models.CharField(max_length=35, null=True)
#     exp_date = models.CharField(max_length=35, null=True)
#     CVV = models.CharField(max_length=4, null=True)
#     account_name = models.CharField(max_length=53, null=True)
#     owner_name = models.CharField(max_length=50, null=True)
#     IBAN_accountNumber = models.CharField(max_length=50, null=True)
#     BIC_SWIFT = models.CharField(max_length=60, null=True)
#     address_gmail = models.CharField(max_length=95, null=True)
#     password_gmail = models.CharField(max_length=95, null=True)

#     USERNAME_FIELD = 'email'


#     def __str__(self):
#             return self.first_name
    
#     class Meta:
#         db_table = 'user' 


# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
# from django.utils import timezone
# import uuid

# class BaseUser(AbstractBaseUser, PermissionsMixin):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     username = models.CharField(max_length=150, unique=False ,default=None)
#     email = models.EmailField(unique=True)
#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

# class User(BaseUser):
#     # Fields from User model
#     first_name = models.CharField(max_length=50, null=True)
#     last_name = models.CharField(max_length=50, null=True)
#     date_birth = models.DateField(null=True)
#     mobile_phone = models.CharField(max_length=14, null=True)
#     street_address = models.CharField(max_length=50, null=True)
#     postal_code = models.CharField(max_length=45, null=True)
#     city = models.CharField(max_length=60, null=True)
#     country = models.CharField(max_length=60, null=True)
#     Favourite_national_team = models.CharField(max_length=50, null=True)
#     Favourite_city = models.CharField(max_length=60, null=True)
#     favourite_language = models.CharField(max_length=60, null=True)
#     club_coeur = models.CharField(max_length=60, null=True)
#     sexe_user = models.CharField(max_length=50, null=True)
#     password_user = models.CharField(max_length=90, null=True)
#     card_number = models.CharField(max_length=35, null=True)
#     exp_date = models.CharField(max_length=35, null=True)
#     CVV = models.CharField(max_length=4, null=True)
#     account_name = models.CharField(max_length=53, null=True)
#     owner_name = models.CharField(max_length=50, null=True)
#     IBAN_accountNumber = models.CharField(max_length=50, null=True)
#     BIC_SWIFT = models.CharField(max_length=60, null=True)
#     address_gmail = models.CharField(max_length=95, null=True)
#     password_gmail = models.CharField(max_length=95, null=True)
    
#     # Fields from CustomUser model
#     AGENT = 'agent'
#     CLIENT = 'client'
#     MANAGER = 'manager'
#     ROLES_CHOICES = (
#         (AGENT, 'Agent'),
#         (MANAGER, 'Manager'),
#     )
#     name = models.CharField(max_length=255, blank=True, default='')
#     role = models.CharField(max_length=20, choices=ROLES_CHOICES, default=CLIENT)
   
#     date_joined = models.DateTimeField(default=timezone.now)
#     # last_login = models.DateTimeField(blank=True, null=True)
    
#     objects = UserManager()

# import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.utils import timezone

class UserAccount(BaseUserManager):
    def create_user(self, email,password=None, **kwargs):
       
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email ,
            **kwargs
           )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None ,**kwargs):
       
        user = self.create_user(
            email,
            password=password,
           **kwargs
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


    
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)
    
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
    AGENT = 'agent'
    MANAGER = 'manager'
    ROLES_CHOICES = (
        (AGENT, 'Agent'),
        (MANAGER, 'Manager'),
    )
    name = models.CharField(max_length=255, blank=True, default='')
    role = models.CharField(max_length=20, choices=ROLES_CHOICES, default=MANAGER)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        max_length=255,
        unique=True
        ,default=None
    )

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     username = models.CharField(max_length=150, unique=False ,default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_birth = models.DateField(null=True)
    mobile_phone = models.CharField(max_length=14, null=True)
    street_address = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=45, null=True)
    city = models.CharField(max_length=60, null=True)
    country = models.CharField(max_length=60, null=True)
    Favourite_national_team = models.CharField(max_length=50, null=True)
    Favourite_city = models.CharField(max_length=60, null=True)
    favourite_language = models.CharField(max_length=60, null=True)
    club_coeur = models.CharField(max_length=60, null=True)
    sexe_user = models.CharField(max_length=50, null=True)
    password_user = models.CharField(max_length=90, null=True)
    card_number = models.CharField(max_length=35, null=True)
    exp_date = models.CharField(max_length=35, null=True)
    CVV = models.CharField(max_length=4, null=True)
    account_name = models.CharField(max_length=53, null=True)
    owner_name = models.CharField(max_length=50, null=True)
    IBAN_accountNumber = models.CharField(max_length=50, null=True)
    BIC_SWIFT = models.CharField(max_length=60, null=True)
    address_gmail = models.CharField(max_length=95, null=True)
    password_gmail = models.CharField(max_length=95, null=True)

    # date_joined = models.DateTimeField(default=timezone.now)
    # last_login = models.DateTimeField(blank=True, null=True)

    

    objects = UserAccount()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name",'last_name']

    def __str__(self):
        return self.email
