from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<uuid:pk>', views.profile, name="profile"),
    path('profile/<uuid:pk>/update', views.edit_account, name="edit-account"),
    path('login', views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    path("register", views.registerUser, name="register"),
    path("account", views.userAccount, name="account"),
    # skill
    path("skill/create", views.skill_create, name="skill-create"),
    path("skill/update/<uuid:pk>", views.skill_update, name="skill-update"),
    path("skill/delete/<uuid:pk>", views.skill_delete, name="skill-delete"),
    # message
    path('inbox/', views.inbox, name="inbox"),
    path('message/<uuid:pk>/', views.viewMessage, name="message"),
    path('create-message/<uuid:pk>/', views.createMessage, name="create-message"),

]