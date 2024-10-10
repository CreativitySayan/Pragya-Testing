from django.contrib import admin
from django.urls import path, include
from certificates import views  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-excel/', views.upload_excel, name='upload_excel'),
    path('check-certificate/', views.check_certificate, name='check_certificate'),
    path('', views.home, name='home'),  # Add this line for the home page
]
