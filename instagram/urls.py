from django.urls import path
from .views import index, profile, follow, story_modal, commentList, like, chat, explore,trending,market

urlpatterns = [
    path('index', index, name = 'index'),
    path('story_modal', story_modal, name='story_modal'),
    path('like', like, name='like'),
    path('commentList', commentList, name='commentList'),
    path('profile/<slug:username>', profile, name="profile"),
    path('<username>/follow', follow, name='follow'),
    path('chat/',chat,name='chat'),
    path('explore/',explore,name = 'explore'),
    path('trending/',trending,name='trending'),
    path('market/',market,name='market')
    
]
