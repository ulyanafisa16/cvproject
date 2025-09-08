from django.urls import path
from .views import (
    ProfileView,
    SkillView,
    PortfolioListView,
    PortfolioDetailView,
    ContactMessageView,
    SkillDetailView,
    ContactMessageDetailView,
    ProfileDetailView
)

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile-api'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('skills/', SkillView.as_view(), name='skills-api'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail-api'),
    path('portfolios/', PortfolioListView.as_view(), name='portfolio-list-api'),
    path('portfolios/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail-api'),
    path('contact/', ContactMessageView.as_view(), name='contact-api'),
    path('contact/<int:pk>/', ContactMessageDetailView.as_view(), name='message-detail-api'),
]
