from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('creative-mind/contact-poll/', include('contact_poll.urls')),
]

# urlpatterns += ""
