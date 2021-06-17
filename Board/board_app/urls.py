from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.sil_post, name='post'),
    path('post/<int:pk>', views.posting, name='posting'),
    path('post/delete/<int:pk>', views.boardDelete, name='delete'),
    path('comment_new/<int:post_pk>', views.comment_new, name='comment_new'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
