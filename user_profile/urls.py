from . import views
from django.urls import path


urlpatterns = [
    path("user_profile", views.user_profile_page, name="user_profile"),
]
