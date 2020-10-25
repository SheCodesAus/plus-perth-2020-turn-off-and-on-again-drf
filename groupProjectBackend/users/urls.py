from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/',views.CustomUserList.as_view()),
    path('users/me', views.MeView.as_view()),
    path('users/<int:pk>', views.CustomUserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)