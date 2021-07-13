from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path("<int:user_id>/profile/", views.profile_view, name='profile'),
    path("update_profile/<int:profile_id>", views.update_profile, name='update_profile')

]
