from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostAdList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('feature', views.feature, name='feature'),
    path('post/new', views.post_new, name='post_new'),
    

]
