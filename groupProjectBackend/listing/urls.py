from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('listing/',views.ListingList.as_view()),
    path('listing/<int:pk>', views.ListingDetail.as_view(), name='listing_detail'),
    path('types/', views.TypeList.as_view()),
    path('types/<slug:slug>', views.TypeDetail.as_view(),name='type_detail'),
    path('locations/', views.LocationList.as_view()),
    path('locations/<slug:slug>', views.LocationDetail.as_view(),name='location_detail'),
    path('levels/', views.LevelList.as_view()),
    path('levels/<slug:slug>', views.LevelDetail.as_view(),name='level_detail'),
    path('audiences/', views.AudienceList.as_view()),
    path('audiences/<slug:slug>', views.AudienceDetail.as_view(),name='audience_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)