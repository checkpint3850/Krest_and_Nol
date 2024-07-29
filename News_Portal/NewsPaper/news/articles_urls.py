from django.urls import path
from .views import PostsList, PostDetail, PostsSearch, ArticleCreate, PostUpdate, PostDelete

urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostsSearch.as_view()),
   path('create/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete')
]
