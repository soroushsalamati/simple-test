from django.urls import path
from poster_app.views import (
    Post,
    PostList,
    PostDetails,
)


urlpatterns = [
    path('post', Post.as_view()),
    path('post-list', PostList.as_view()),
    path('post/<int:pk>', PostDetails.as_view()),

]
