from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from songcrud_api import views

urlpatterns = [
    path('song/', views.song_list),
    path('song/<int:pk>/', views.song_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)