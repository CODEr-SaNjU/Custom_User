from django.contrib.auth.models import User
from django.shortcuts import render
from .models import UserProfile
from .forms import UserProfileCreationForm,UserProfileChangeForm
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'Frontend_files/userprofile_list.htm'



class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileCreationForm
    template_name = "Frontend_files/userprofile_create.htm"
    success_url = '/'


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileCreationForm
    template_name = "Frontend_files/userprofile_create.htm"


class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = ".html"
