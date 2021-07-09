from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Contact



class Index(TemplateView):
    template_name = "contact_poll/index.html"

class ContactForm(CreateView):
    template_view = "contact_poll/contact_form.html"
    model = Contact
    fields = [
        'first_name',
        'last_name',
        'email',
        'state',
        'occupation'
    ]
    success_url = reverse_lazy('contact_poll_index')

    
