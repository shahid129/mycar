from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostAdList.as_view(), name="home"),
    path('post_your_add_edit/<post_id>',
         views.post_your_add_edit, name='post_your_add_edit'),
    path('post_your_add_delete/<post_id>',
         views.post_your_add_delete, name='post_your_add_delete'),
    path('post_your_add', views.post_your_add, name='post_your_add'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path('like/<slug:slug>/', views.PostAdLike.as_view(), name='post_like'),
    # link to search car page
    path("search_car", views.search_car, name="search_car"),
    path('<slug:slug>/', views.search_car,
         name='search_car'),  # link to searched car
    path('activate/<uidb64>/<token>',
         views.Verification.as_view(), name='activate'),
    path('about', views.about, name='about'),
]
