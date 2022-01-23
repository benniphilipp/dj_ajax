from django.urls import path
from .views import (
    post_list_and_create,
    hello_wold_view,
    load_post_data_view,
    like_unlike_post,
    post_detaile,
    post_detaile_data_view,
    update_post,
    delete_post,
    img_upload_view,
)

app_name = 'postes'

urlpatterns = [
    path('', post_list_and_create, name='main-board'),
    path('hello/', hello_wold_view, name='hello-wold'),
    path('data/<int:num_posts>/', load_post_data_view, name='posts-data'),
    path('like-unlike/', like_unlike_post, name='like-unlike'),
    path('<int:pk>/', post_detaile, name='post-detaile'),
    path('<pk>/data/', post_detaile_data_view, name='post-detaile-data'),
    path('<pk>/update/', update_post, name='post-update'),
    path('<pk>/delete/', delete_post, name='post-deltete'),
    path('upload/', img_upload_view, name='img-upload'),
]
