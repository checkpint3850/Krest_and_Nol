from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, ResponseCreate, ResponseList, ResponseDelete, ConfirmUser, ProfileView


urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='ad_detail'),
   path('search/', PostsList.as_view()),
   path('create/', PostCreate.as_view(), name='ad_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='ad_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='ad_delete'),
   path('responses/', ResponseList.as_view(), name='response_list'),
   path('responses/create', ResponseCreate.as_view(), name='response_create'),
   path('responses/<int:pk>/delete', ResponseDelete.as_view(), name='response_delete'),
   path('confirm/', ConfirmUser.as_view(), name='confirm_user'),
   path('profile/', ProfileView.as_view(), name='profile'),
]

