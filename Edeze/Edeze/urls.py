"""
URL configuration for Edeze project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home.views import *

urlpatterns = [
    path("",index,name="home"),
    path("success-page/",success),
    path("admin/", admin.site.urls),
    path("register/",register_user),
    path("login/",login_user),
    path("home/",home),
    path("logout/",logout_user),
    path("training/",training_page),
    path("<id>/trainingDetails/",training_details),
    path("<user_id>/<course_id>/addtocart",addtocart),
    path("<id>/cart/",cart),
    path("consulting/",consulting),
    path("<id>/consultingDetails/",consultingDetails),
    path("webstore/",webstore),
    path("<id>/webstoreDetails/",webstoreDetails),
    path("<user_id>/<course_id>/addtocartwebstore",addtocartwebstore),
    path("aboutus/",about_us)

]
