""
from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from graphs import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphs/', include('graphs.urls')),

]

