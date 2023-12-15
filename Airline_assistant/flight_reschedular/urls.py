from django.contrib import admin
from django.urls import path,include
from flight_reschedular import views

urlpatterns = [
    path("", views.home,name='Generate'),
    path("generate", views.request_page),
    path("submit", views.generate)
    # path("visit/<slug:place>",views.visit)
]