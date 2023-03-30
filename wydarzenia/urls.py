from django.urls import path

from . import views

urlpatterns = [
    path("login_page/", views.login_page, name="login_page"),
    path("logout/", views.logout_user, name="logout"),
    path("register_page/", views.register_page, name="register_page"),
    path("", views.home, name="home"),
    path("room/<int:pk>/", views.room, name="room"),
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<int:pk>/", views.update_room, name="update-room"),
    path("delete-room/<int:pk>/", views.delete_room, name="delete-room"),
    path("history/", views.history, name="history"),
    path("profile/<int:pk>/", views.profile, name="profile"),
]
