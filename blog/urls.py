from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostAdList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post_your_add', views.post_your_add, name='post_your_add'),
]
