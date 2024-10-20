from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, CategoryListView, subscribe


urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostsList.as_view()),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe/', subscribe, name='subscribe')
]
