"""
URL configuration for dproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name="home"),
    path("Login",views.Login,name="login"),
    path("Register",views.Register,name="Register"),
    path("admindashboard",views.admindashboard,name="admindashboard"),
    path("customerdetails",views.customerdetails,name="customerdetails"),
    path("userdashboard",views.userdashboard,name="userdashboard"),
    path("Addevent",views.Addevent,name="Addevent"),
    path("Eventlist",views.Eventlist,name="Eventlist"),
    path("Deletevent/<int:id>",views.Deleteevent,name="Deletevent"),
    path("Updateevent/<int:id>",views.Updateevent,name="Updateevent"),
    path("U_Event/<int:id>",views.U_Event,name="U_Event"),

    path("AvailableEvent",views.AvailableEvent,name="AvailableEvent"),
    path("Book_event/<int:id>",views.Book_event,name="Book_event"),
    path("Orderlist",views.Orderlist,name="Orderlist"),
    path("Payment/<int:id>",views.Payment,name="Payment"),
    path("Payment_success",views.Payment_success,name="Payment_success"),
    path("Logout",views.Logout,name="Logout"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
