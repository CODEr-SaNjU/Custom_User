from django.urls import path
from .views import UserProfileListView , UserProfileCreateView, UserProfileUpdateView ,UserProfileDeleteView,LoginView,LogoutView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',LoginView.as_view(),name='login'),
    path('logout/',login_required(LogoutView.as_view()),name="logout"),
    path('user-list/', login_required(UserProfileListView.as_view()), name="userprofileview"),
    path('add-user/',UserProfileCreateView.as_view(),name='userprofilecreate'),
    path('user/<int:pk>/update/',login_required(UserProfileUpdateView.as_view()),name='userprofileupdate'),
    path('user/<int:pk>/delete/',login_required(UserProfileDeleteView.as_view()),name='userprofiledelete')
]
