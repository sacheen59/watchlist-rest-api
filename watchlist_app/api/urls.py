from django.urls import path
from . import views

urlpatterns = [
    path('',views.WatchListAV.as_view(), name = 'watchlist'),
    path('<int:pk>/',views.WatchListDetailAV.as_view(), name = 'watchlist-detail'),
    path('platform/',views.StreamPlatfromAV.as_view(), name = "streamPlatform"),
    path('platform/<int:pk>/',views.StreamPlatformDetailAV.as_view(), name = "streamPlatform-detail"),
]