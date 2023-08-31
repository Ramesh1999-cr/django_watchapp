
from django.urls import path,include
from rest_framework.routers import DefaultRouter


from watchlist_app.views import (StreamPlatformAV,StreamPlatformVS,StreamPlatformDetailAV,WatchListAV,
                                 WatchDetailAV,WatchListGV,ReviewList,ReviewDetail,ReviewCreate,UserReview)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('streampl/', StreamPlatformAV.as_view(), name='str`eam-list'),
    path('streampl/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('',include(router.urls)),

    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('reviews/', UserReview.as_view(), name='user-review-detail'),

]


