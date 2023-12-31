from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<uuid:pk>', views.profile, name="profile"),
    path('login', views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    path("register", views.registerUser, name="register"),
    path("account", views.userAccount, name="account"),
    # skill
    path("skill/create", views.skill_create, name="skill-create"),
    path("skill/update/<uuid:pk>", views.skill_update, name="skill-update"),
    path("skill/delete/<uuid:pk>", views.skill_delete, name="skill-delete"),
]