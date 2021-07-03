from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect,HttpResponse
from .models import UserProfile
from django.conf import settings
from django.contrib import messages
from .forms import UserProfileCreationForm,UserProfileChangeForm
from django.views.generic import ListView, UpdateView, DeleteView, CreateView,View
from django.contrib.auth import authenticate ,login,logout

class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'Frontend_files/userprofile_list.htm'

class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileCreationForm
    template_name = "Frontend_files/userprofile_create.htm"
    success_url = '/userprofileview/'


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileCreationForm
    template_name = "Frontend_files/userprofile_update.htm"
    success_url = '/userprofileview/'

class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = "Frontend_files/userprofile_delete.htm"
    success_url = '/userprofileview/'



class LoginView(View):
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('userprofileview')
            else:
                return HttpResponse("Inactive user.")
        else:
            messages.error(
                request, 'Error! please enter the correct  Email address and Password for login.')
            return HttpResponseRedirect('/')


    def  get(self,request):
        return render(request,"Frontend_files/login.htm")
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
