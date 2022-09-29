
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("BookUae", views.BookUae, name='BookUae'),
    path("Pakistanhotels", views.Pakistanhotels, name='Pakistanhotels'),
    path("Uaehotels", views.Uaehotels, name='Uaehotels'),
    path("Otherhotels", views.Otherhotels, name='Otherhotels'),
    path("Others", views.Others, name='Others'),
    path("Uae", views.Uae, name='Uae'),
    path("Pakistan", views.Pakistan, name='Pakistan'),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services'),
    path("ticket", views.ticket, name='ticket'),
    path("info", views.info, name='info'),
    path("info2", views.info2, name='info2'),
    path("uaeticket", views.uaeticket, name='uaeticket'),
    path("signup", views.Signup, name='signup'),
]
