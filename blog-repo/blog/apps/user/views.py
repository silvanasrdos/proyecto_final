from django.shortcuts import render
from blog.views import TemplateView

# Create your views here.
class UserProfileView(TemplateView):
    template_name = 'user/user_profile.html'