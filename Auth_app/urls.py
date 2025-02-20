
from django.urls import path
from django.urls.conf import include
from .views import user_signup, user_login, dashboard, user_logout

urlpatterns = [
    path('register/', user_signup, name='register'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
    path('', user_login, name='login'),
    
]
