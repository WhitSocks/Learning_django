"""
URL configuration for my_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
def welcome(request):
    welcome_message = (
        "<ul>\n"
        "<li><h1>Welcome to My App!<h1></li>\n"
        "<li>This is a list-based welcome page.</li>\n"
        "<li>Here are some features of this API:</li>\n"
        "<li>1. <a href='/Capture-Information/drones' >Capture-Information/drones</a></li>\n"
        "<li>2. <a href='/Capture-Information/medications'>Capture-Information/medications</a></li>\n"
        "<li>3. <a href='/Capture-Information/Load/drone'>Capture-Information/Load/drone</a></li>\n"
        "<li>4. <a href='/Capture-Information/batterylogs'>Capture-Information/batterylogs</a></li>\n"
        "<li>5. <a href='/battery_info/drones_with_low_battery/?battery_capacity=100'> battery_info/drones_with_low_battery/?battery_capacity=100 </a></li>\n"
        "<li>6. <a href='/battery_info/drones_battery/?serial_number=137984625'> battery_info/drones_battery/?serial_number=137984625 </a></li>\n"
        "</ul>\n"
        "<p>Thank you for using My App!</p>\n"
    )
    return HttpResponse(welcome_message)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome), # home page
    path('',include('my_project.urls'))
    
]
