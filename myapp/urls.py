from django.urls import path
from.views import *
urlpatterns = [
    path('',index,name='index'),
    path('register/',register,name='register'),
    path('register_submit/', register_submit, name='register_submit'),
    path('login/',login,name='login'),
    path('otp/',otp,name='otp'),
    path('total_user/',total_user,name='total_user'),
    path('add_user/',add_user,name='add_user'),
    path('buy_now/<int:pk>', buy_now, name='buy_now'),
    path('buy_now/paymenthandler/', paymenthandler, name='paymenthandler'),

    

]