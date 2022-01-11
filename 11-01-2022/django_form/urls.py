from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from myapp import contact
 
urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', contact.index),    
    path('contact/', contact.contact, name='contact'),  
]from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from myapp import contact
 
urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', contact.index),    
    path('contact/', contact.contact, name='contact'),  
]