from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class UserDetail(models.Model):
        SEX_CHOICES = ((True,'Male'),(False,'Female'))
        STATE_CHOICES = (("Andaman & Nicobar Islands",'Andaman & Nicobar Islands'),
            ("Andhra Pradesh",'Andhra Pradesh'),
            ("Arunachal Pradesh",'Arunachal Pradesh'),
            ("Assam",'Assam'),
            ("Bihar",'Bihar'),
            ("Chandigarh",'Chandigarh'),
            ("Chhattisgarh",'Chhattisgarh'),
            ("Dadra & Nagar Haveli",'Dadra & Nagar Haveli'),
            ("Daman and Diu",'Daman and Diu'),
            ("Delhi",'Delhi'),
            ("Goa",'Goa'),
            ("Gujarat",'Gujarat'),
            ("Haryana",'Haryana'),
            ("Himachal Pradesh",'Himachal Pradesh'),
            ("Jammu & Kashmir",'Jammu & Kashmir'),
            ("Jharkhand",'Jharkhand'),
            ("Karnataka",'Karnataka'),
            ("Kerala",'Kerala'),
            ("Lakshadweep",'Lakshadweep'),
            ("Madhya Pradesh",'Madhya Pradesh'),
            ("Maharashtra",'Maharashtra'),
            ("Manipur",'Manipur'),
            ("Meghalaya",'Meghalaya'),
            ("Mizoram",'Mizoram'),
            ("Nagaland",'Nagaland'),
            ("Odisha",'Odisha'),
            ("Puducherry",'Puducherry'),
            ("Punjab",'Punjab'),
            ("Rajasthan",'Rajasthan'),
            ("Sikkim",'Sikkim'),
            ("Tamil Nadu",'Tamil Nadu'),
            ("Telangana",'Telangana'),
            ("Tripura",'Tripura'),
            ("Uttarakhand",'Uttarakhand'),
            ("Uttar Pradesh",'Uttar Pradesh'),
            ("West Bengal",'West Bengal'),
            )
        usr = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
        auth_token = models.CharField(max_length=100, default="")
        is_verified = models.BooleanField(default=False)
        dob = models.DateField(null = True)
        photo = models.ImageField(default='user-profile.png',upload_to='Profiles/',null=True)
        mobile = models.CharField(max_length=10,null=True, default='')
        alternate_mobile = models.CharField(max_length=10,null=True,blank=True,default='')
        address = models.TextField(default='')
        pincode = models.CharField(max_length=6, null=True, default='')
        locality = models.CharField(max_length=100, null=True, blank=True,default='')
        city = models.CharField(max_length=100, null=True, blank=True,default='')
        state = models.CharField(max_length=50,choices=STATE_CHOICES, null=True,default='')
        sex = models.BooleanField(choices=SEX_CHOICES, null=True,default='')
        
        @property
        def imageURL(self):
            try:
                 url = self.photo.url
            except:
                 url = ''
            return url
        
                    

class Contact(models.Model):
        date = models.DateField(auto_now=True)
        name = models.CharField(max_length=100)
        email = models.EmailField()
        subject = models.CharField(max_length=100)
        phone = models.CharField(max_length=10)
        message = models.TextField()
        
        def __str__(self):
            return self.email


class ReviewRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    fn = models.CharField(max_length=50, blank=True)
    ln = models.CharField(max_length=50, blank=True)
    img = models.ImageField(null=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fn