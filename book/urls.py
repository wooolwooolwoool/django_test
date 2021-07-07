from django.urls import path
from . import views

urlpatterns = [
    # トップページ
    path('', views.top, name='top'), 
    # 本棚一覧
    path('list/', views.BookList.as_view(), name='book_list'), 
    # 本棚追加
    path('add/', views.add_post, name='add_post'), 
    # 本棚詳細
    path('detail/<int:pk>/', views.book_detail, name='book_detail'),
    # 本の検索（ユーザーからはアクセスされない想定）
    path('serch/<str:key>/', views.book_serch, name='book_serch'),
]