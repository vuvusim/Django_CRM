from django.contrib import admin
from django.urls import path, include
from leads.views import home_page, second_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', second_page),
]
