from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_poll/', include('contact_poll.urls')),
]

# urlpatterns += ""
