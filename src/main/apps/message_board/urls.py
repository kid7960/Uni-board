from django.urls import path
from .views import (
    Message_Board,
    Post_Detail,
    Create_Post,
    Update_Post,
    Delete_Post,
    My_Posts,
    like_post_mb,
    like_post_mp,
    like_post_pd

)

urlpatterns = [
    path('',                    Message_Board.as_view(),    name='message_board'),
    path('<int:pk>/',           Post_Detail.as_view(),      name='post_detail'  ),
    path('create/',             Create_Post.as_view(),      name='create_post'  ),
    path('<int:pk>/update/',    Update_Post.as_view(),      name='update_post'  ),
    path('<int:pk>/delete/',    Delete_Post.as_view(),      name='delete_post'  ),
    path('my_posts/',           My_Posts.as_view(),         name='my_posts'     ),
    path('like_post_mb/<int:pk>',  like_post_mb,            name='like_post_mb'  ),
    path('like_post_mp/<int:pk>',  like_post_mp,            name='like_post_mp' ),
    path('like_post_pd/<int:pk>',  like_post_pd,            name='like_post_pd' ),
]