"""NEWVF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout
from django.urls import path, re_path
from vehicle import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contactus/', views.contact_us, name='contact'),
    # vehicle urls
    path('car/', views.CarList, name='car_list'),
    path('car/create/', views.CreateCar.as_view(), name='car_create'),
    re_path(r'^car/(?P<id>[0-9]+)/$', views.CarDetails, name='car_details'),
    # auth urls
    re_path(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name="logout"),
    # profile urls
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "VehicleFinder Admin"
admin.site.site_title = "VehicleFinder Admin Portal"
admin.site.index_title = "Welcome to VehicleFinderPortal"
