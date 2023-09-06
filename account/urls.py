
from django.urls import path
from account.views import *

from django.contrib.auth.views import LoginView
from .forms import LoginForm


urlpatterns = [
    # users
    path('register',login_page,name='register'),  
    path('profile',edit_profile,name='profile'), 
    path('logout/', logout_view, name='logout'), 

    path('dashboard/',dashboard_page,name='dashboard'),  
    path('orders/',order_page,name='orders'),  
    path('notification/',notification_page,name='notification'),  
    path('payments/',payment_page,name='payments'),  
    path('resales/',resales_page,name='resales'),  
    path('document/',document_page,name='documents'),  
    # path('profile',edit_profile,name='profile'),  

    path('login/', LoginView.as_view(template_name='account/login.html', form_class=LoginForm), name='login')

]