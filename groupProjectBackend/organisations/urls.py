from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('organisations/',views.OrganisationList.as_view()),
    path('organisations/<slug:slug>', views.OrganisationDetail.as_view(), name='organisation_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)