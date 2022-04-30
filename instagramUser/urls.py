from django.urls import path
from .views import signup, user_login,settings, CreatePost

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('', user_login, name = 'user_login'),
    path('settings/<slug:username>',settings,name = 'settings'),
    path('CreatePost/',CreatePost.as_view(),name = 'createpost')
]
