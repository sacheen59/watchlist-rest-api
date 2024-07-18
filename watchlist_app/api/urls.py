from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()
router.register('stream',views.StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    path('',views.WatchListAV.as_view(), name = 'watchlist'),
    path('<int:pk>/',views.WatchListDetailAV.as_view(), name = 'watchlist-detail'),
    # path('platform/',views.StreamPlatfromAV.as_view(), name = "streamPlatform"),
    # path('platform/<int:pk>/',views.StreamPlatformDetailAV.as_view(), name = "streamPlatform-detail"),
    path('',include(router.urls)),
    # path('reviews/',views.ReviewListAV.as_view(), name="review-list"),
    # path('reviews/<int:pk>/',views.ReviewListDetailAV.as_view(),name = "review-detail"),
    path('stream/<int:pk>/review-create/',views.CreateReview.as_view(), name = "review-create"),
    path('stream/<int:pk>/review/',views.ReviewListAV.as_view(), name = "review-list"),
    path('stream/review/<int:pk>/',views.ReviewListDetailAV.as_view(), name = "review-detail"),
]