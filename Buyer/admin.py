from django.contrib import admin
from .models import UserDetail, Contact, ReviewRating
# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Contact)
admin.site.register(ReviewRating)