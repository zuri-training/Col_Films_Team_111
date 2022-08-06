from django.urls import path
from .views import get_reg, get_otp, create_user
urlpatterns = [
    path('get_reg/', get_reg, name="get_reg"),
     path('get_otp/', get_otp, name="get_otp"),
      path('create_user/', create_user, name="create_user"),
]


