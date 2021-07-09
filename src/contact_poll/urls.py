from django.urls import path

from .views import ContactForm, Index

urlpatterns = [
    path('', Index.as_view(), name="contact_poll_index"),
    path('contact/form/', ContactForm.as_view(), name="contact_form"),
]