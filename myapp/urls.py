from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("contact/list/", views.contactList.as_view()),
    path("contactDetailById/<int:pk>", views.contactDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
