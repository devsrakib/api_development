from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns(
    [
        path("", views.api_root),
        path("contact/list/", views.contactList.as_view(), name="contact-list"),
        path("contactDetailById/<int:pk>", views.contactDetails.as_view()),
    ]
)
