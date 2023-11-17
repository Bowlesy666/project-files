from . import views
from django.urls import path


urlpatterns = [
    path('profile_list/', views.ProfileList.as_view(), name='profile_list'),
    path('<slug:slug>/', views.ProfileDetail.as_view(), name='profile_detail'),
]
