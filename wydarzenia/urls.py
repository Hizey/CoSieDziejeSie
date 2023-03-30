from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_page, name="register"),
    path("", views.home, name="home"),
    path("room/<int:pk>/", views.room, name="room"),
    # path("profile/<int:pk>", views.user_profile, name="user-profile"),
    path("create-room/", views.create_room, name="create-room"),
    # path("profile/<int:pk>/", views.user_profile, name="user-profile"),
    path("update-room/<int:pk>/", views.update_room, name="update-room"),
    path("delete-room/<int:pk>/", views.delete_room, name="delete-room"),
    path("history/", views.history, name="history"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("delete-message/<int:pk>/", views.delete_message, name="delete-message"),
]
