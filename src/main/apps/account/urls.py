from django.urls import path, include
from main.apps.account import views as user_views
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("",            user_views.account,                                                      name="account"  ),
    path('register/',   user_views.register,                                                     name='register' ),
    path('login/',      auth_views.LoginView.as_view(   template_name='account/login.html'    ), name='login'    ),
    path('logout/',     auth_views.LogoutView.as_view(  template_name='account/logout.html'   ), name='logout'   ),
    path('profile/',    user_views.profile,                                                      name='profile'  ),
]