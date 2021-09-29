"""SkyTravel URL Configuration

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
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', userLogin, name="user-login"),
    path('registration/', userRegistration, name='user-registration'),
    path('', dashboard, name='dashboard'),
    path('air/', air, name="air"),
    path('bus/', bus, name="bus"),
    path('book-trip/air/<int:id>/', bookTripAir, name="book-trip-air"),
    path('book-trip/bus/<int:id>/', bookTripBus, name="book-trip-bus"),
    path('pay/Bus/<int:id>/', payBus, name="paybus"),
    path('pay/Air/<int:id>/', payAir, name="payair"),
    path('mytrip-bus/', mytripBus, name="mytrip-bus"),
    path('incomplete-air/', incompleteAir, name="incomplete-air"),
    path('incomplete-bus/', incompleteBus, name="incomplete-bus"),
    path('mytrip-air/', mytripAir, name="mytrip-air"),
    path('ticket/Bus/<int:id>/', busticket, name="busticket"),
    path('ticket/Air/<int:id>/', airticket, name="airticket"),
    path('invoice/Bus/<int:id>/', businvoice, name="busticket"),
    path('invoice/Air/<int:id>/', airinvoice, name="airticket"),
    path('log-out/', logOut, name="log-out"),
]
