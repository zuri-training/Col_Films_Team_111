from django.urls import path
from django.contrib.auth import views as auth_views

from .views import get_reg, get_otp, create_user, user_login, user_logout
urlpatterns = [
    path('get_reg/', get_reg, name="get_reg"),
    path('get_otp/', get_otp, name="get_otp"),
    path('create_user/', create_user, name="create_user"),
    path('user_login/', user_login, name= 'user_login' ),
    path('user_logout', user_logout, name= 'user_logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name = 'reset_password'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]


