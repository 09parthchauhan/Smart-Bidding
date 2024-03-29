"""Auction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'E-Auction'
admin.site.site_title = 'E-Auction Admin'
#admin.site.site_url = 'http://eauction.com/'
admin.site.index_title = ''
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Buyer.urls'),name='home'),
    path('seller/',include('Seller.urls')),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='forgot_password.html'), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='changepassword.html',success_url = '/'),name='change_password'),
    path('seller/change-password/',auth_views.PasswordChangeView.as_view(template_name='seller/changepassword.html',success_url = '/'),name='change_password1'),
    path('verification/', include('verify_email.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
