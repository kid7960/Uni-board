from django.urls import path
from .views import (
    Message_Board,
    Post_Detail,
    Create_Post,
    Update_Post,
    Delete_Post,
    My_Posts,
    Search_Posts,
    Add_Comment,
    Delete_Comment,
    like_post
)

urlpatterns = [
    path('',                    Message_Board.as_view(),    name='message_board'),
    path('<int:pk>/',           Post_Detail.as_view(),      name='post_detail'  ),
    path('create/',             Create_Post.as_view(),      name='create_post'  ),
    path('<int:pk>/update/',    Update_Post.as_view(),      name='update_post'  ),
    path('<int:pk>/delete/',    Delete_Post.as_view(),      name='delete_post'  ),
    path('my_posts/',           My_Posts.as_view(),         name='my_posts'     ),
    # Search Post, Comment and Likes
    path('search_posts/',                           Search_Posts.as_view(),     name='search_posts'     ),
    path('<int:pk>/add_comment/',                   Add_Comment.as_view(),      name='add_comment'      ),
    path('<int:pk>/delete_comment/',                Delete_Comment.as_view(),   name='delete_comment'   ),
    path('like_post/<int:pk>#<path:current_url>',   like_post,                  name='like_post'        ),
]