django models va forms validations
django biz ma'lumotlarni tekshirish(maydonlarimizni) tekshirish uchan validations dan foydalanamiz

models.py da ishlatib ko'ramiz
```python
from django.db import models
""" Qiymat Xatoligini qaytarish uchun ValidationError dan foydalanamiz """
"""Django'da ValidationError klassi ma'lumotlarni tekshirish muvaffaqiyatsiz bo'lganda xatoni ko'tarish uchun ishlatiladi"""
from django.core.exceptions import ValidationError

""" Bu bizning field(maydon) qiymatlari max uzinligi(Length) yoki min uzinligi(Length) larni boshqarishga yordam beradi--> MaxLengthValidator, MinLengthValidator"""
from django.core.validators import MaxLengthValidator, MinLengthValidator


# bizning functsiya
def validation_name(value):
    if len(value)<=10 or len(value)>=250:
        raise ValidationError("name 10 dan katta va 250 dan kichik bo'lsin")

class Category(models.Model):
    """ 1 chi usilda biz djangoni o'zinging MaxLengthValidator va MinLengthValidator class lardan foydalandik"""
    # name = models.CharField(max_length=250, validations=[MaxLengthValidator(250), MinLengthValidator(10)])

    """ 2 chi usilda biz o'zimiz tuzgan funksiyalardan ma'lumotlarni tekshiramiz """
    name = models.CharField(max_length=250, validations=[validation_name()])
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntagerField()

    def __str__(self):
        return self.name
    def clean(self):
        if self.prise<=10:
            raise ValidationError("Price 10 dan kam bo'lmasin")

        
    



    
```
