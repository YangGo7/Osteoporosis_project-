from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name='board'),  # 게시판 페이지
    path('create/', views.create_post, name='create_post'),  # 게시글 작성 페이지
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # 게시글 조회 페이지
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),  # 게시글 수정 페이지
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),  # 게시글 삭제 기능
    path('<int:post_id>/reply/', views.create_reply, name='create_reply'),
    path('<int:post_id>/like/', views.toggle_like, name='toggle_like'),  # 추가
    path('reply/<int:reply_id>/like/', views.toggle_reply_like, name='toggle_reply_like'),  # 추가
]
