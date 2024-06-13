from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.template.defaultfilters import slugify

def get_roundam_code():
    code = str(uuid.uuid4)[:10]
    return code

"""" price ni validations ga teksirish 1 usil """
# def price_value(value):
#     if value < 10:
#         raise ValidationError('Price cannot be negative')
#     return value

class Products(models.Model):
    name = models.CharField(max_length=125)
    slug = models.SlugField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[price_value])
    old_prise = models.DecimalField(max_digits=10, decimal_places=2, validators=[price_value])
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def get_foiz(self):
        foiz = str(int(self.price)*100/int(self.old_prise))
        return foiz
    
    def get_absolute_url(self):
        return reverse("product_datile", kwargs={"slug": self.slug})
    
    
    def __str__(self):
        return self.name
    
    """ price 10 dan kam bo'lmasligini tekishramiz 2 usilda """
    def clean(self):
        if self.price < 10:
            raise ValidationError("Price 10 dan kam bo'lmasin!!")
        
    def save(self, *args, **kwargs):
        ex = False
        now_slug = slugify(str(self.name)+""+str(self.description))
        ex = Products.objects.filter(slug=now_slug).exists()
        while ex:
            now_slug = slugify(now_slug+""+get_roundam_code())
            ex = Products.objects.filter(slug=now_slug).exists()
            
        self.slug = now_slug
        super(Products, self).save(*args, **kwargs)
        