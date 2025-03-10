"""
URL configuration for SPARS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from sparsapp.views import*
from sparsapp.hooks import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index ,name='index'),
    path('search/', search),
    path('search/', search),
    path('predict/<str:ticker_value>/<str:number_of_days>/', predict),
    path('ticker/', ticker),
    path('login/',login),
    path('signup/',signup),
    path('logged/',logged),
    path('loggedout/',loggedout),
    path('profile/',profile),
    path('update_user/',update_user),
    path('updated/',updated),
    path('market/',market),
    path('searchbar/',searchbar),
    path('pay/',pay),
    path('order/',order),
    path('payment_success/', payment_success, name='payment_success'),
    path('payment_cancel/', payment_failed, name='payment_failed'),
    path('otpe/',otpe),
    path('checkotp/',checkotp),
   # path('otp_page/',otp_page),
    #path('trye/',trye),,
    path('paypal_payment_received/',paypal_payment_received),
    path('paypal',include("paypal.standard.ipn.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
