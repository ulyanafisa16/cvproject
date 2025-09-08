from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="dashboard"),
    # ---------------- HOME & LOGIN ----------------
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # ---------------- PROFILE CRUD ----------------
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/add/', views.profile_create, name='profile_create'),
    path('profiles/edit/<int:pk>/', views.profile_edit, name='profile_edit'),
    path('profiles/delete/<int:pk>/', views.profile_delete, name='profile_delete'),

    # ---------------- SKILL CRUD ----------------
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/add/', views.skill_create, name='skill_create'),
    path('skills/edit/<int:pk>/', views.skill_edit, name='skill_edit'),
    path('skills/delete/<int:pk>/', views.skill_delete, name='skill_delete'),

    # ---------------- PORTFOLIO CRUD ----------------
    path('portfolios/', views.portfolio_list, name='portfolio_list'),
    path('portfolios/add/', views.portfolio_create, name='portfolio_create'),
    path('portfolios/edit/<int:pk>/', views.portfolio_edit, name='portfolio_edit'),
    path('portfolios/delete/<int:pk>/', views.portfolio_delete, name='portfolio_delete'),

    # ---------------- PORTFOLIO IMAGE CRUD ----------------
    path('portfolio-images/', views.portfolio_image_list, name='portfolio_image_list'),
    path('portfolio-images/add/', views.portfolio_image_create, name='portfolio_image_create'),
    path('portfolio-images/edit/<int:pk>/', views.portfolio_image_edit, name='portfolio_image_edit'),
    path('portfolio-images/delete/<int:pk>/', views.portfolio_image_delete, name='portfolio_image_delete'),

    # ---------------- CONTACT MESSAGE ----------------
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('messages/delete/<int:pk>/', views.message_delete, name='message_delete'),


]


