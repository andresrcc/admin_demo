from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def hello(request):
    return HttpResponse("Hello, World!")

urlpatterns = [
    path('', hello),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]
