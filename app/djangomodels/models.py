from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
# Create your models here.

# 1 qadam user models tuzamiz
"""
Django-da, maxsus foydalanuvchi modelini 
yaratishda sizda ikkita variant mavjud:
AbstractUser va AbstractBaseUser. 
Ikkalasi ham Django tomonidan taqdim 
etilgan mavhum asosiy sinflardir, ammo 
ular turli maqsadlarga xizmat qiladi. 
"""
# AbstractBaseUser
"""
AbstractBaseUser - bu foydalanuvchi modelining minimal amalga oshirilishi. 
U foydalanuvchi modeli uchun zarur bo'lgan asosiy maydonlar va usullarni 
taqdim etadi, masalan: 
---------------------------------------------------
id (primary key)
password (hashed password)
last_login (datetime of last login)
---------------------------------------------------
"""
# AbstractUser
"""
AbstractUser - bu foydalanuvchi modelining yanada keng qamrovli amalga oshirilishi. 
U AbstractBaseUser-ga asoslanadi va qo'shimcha maydonlar va usullarni qo'shadi, masalan: 
----------------------------------------------------
username (username)
first_name (first name)
last_name (last name)
email (email address)
is_staff (boolean indicating staff status)
is_active (boolean indicating active status)
is_superuser (boolean indicating superuser status)
-----------------------------------------------------
"""
# Asosiy farqlar
"""
AbstractBaseUser minimal amalga oshirishni ta'minlaydi,
AbstractUser esa yanada kengroq amalga oshirishni ta'minlaydi.
AbstractBaseUser barcha maydonlar va usullarni aniqlash 
uchun ko'proq mehnat talab qiladi, AbstractUser esa qutidan 
tashqarida ko'plab maydonlar va usullarni taqdim etadi.
AbstractUser - odatiy foydalanuvchi modeli bilan bir xil 
maydonlar va xatti-harakatlarga ega bo'lgan foydalanuvchi 
modelini yaratmoqchi bo'lganingizda keng tarqalgan tanlovdir.
"""
   
# Umuman olganda, agar siz o'zingizning foydalanuvchi modelingizni yuqori
# darajada sozlash va nazorat qilishni istasangiz, AbstractBaseUser yaxshiroq 
# tanlov bo'lishi mumkin. Agar siz standart foydalanuvchi modeli asosida qurmoqchi
# bo'lsangiz va ba'zi maxsus maydonlar yoki xatti-harakatlar qo'shmoqchi bo'lsangiz, 
# AbstractUser yaxshiroq mos keladi.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    objects = MyUserManager()
    class Meta:
        ordering=['cerated']
    