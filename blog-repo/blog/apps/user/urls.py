from django.urls import path
import apps.user.views as views 

urlpatterns = [
    path('users/profile/', views.UserProfileView.as_view(), name="user_profile")

]