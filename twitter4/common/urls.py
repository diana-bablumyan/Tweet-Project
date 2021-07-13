from django.urls import path
from . import views


urlpatterns = [
    path('send_user_email/', views.send_user_email, name='send_user_email')
]