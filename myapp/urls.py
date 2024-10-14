from django.urls import path
from myapp import views

urlpatterns = [path("contact_list/", views.contact_list)]
