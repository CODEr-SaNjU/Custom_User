from django.urls import path
from .views import UserProfileListView , UserProfileCreateView, UserProfileUpdateView ,UserProfileDeleteView


urlpatterns = [
    path('', UserProfileListView.as_view(), name="userprofileview"),
    path('add-user/',UserProfileCreateView.as_view(),name='userprofilecreate'),
    path('user/<int:pk>/update',UserProfileUpdateView.as_view(),name='userprofileupdate'),
    path('user/<int:pk>/delete',UserProfileDeleteView.as_view(),name='userprofiledelete')
]
