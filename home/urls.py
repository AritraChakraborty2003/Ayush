from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path("main",views.index,name="main"),
    path('login',views.Login,name="login"),
    path('Signup',views.Signup,name="Signup"),
    path('dashboard',views.dashboard,name="dashboard"),
    path("logout",views.logout,name="logout")

]
