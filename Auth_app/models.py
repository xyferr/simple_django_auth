from django.db import models

from django.utils.html import format_html

# Create your models here.
class user_data(models.Model):
    
    USER_TYPE_CHOICES = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    Address = models.TextField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.IntegerField()
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES)
    
    def img_tag(self):
        return format_html('<img src="/static/{}" style="width:40px; height:40px;" />'.format(self.image))
    
    
    