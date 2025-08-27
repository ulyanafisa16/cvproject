from django.urls import path
from .views import ProfileView, SkillView, PortfolioListView, PortfolioDetailView, ContactMessageView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile-api'),
    path('skills/', SkillView.as_view(), name='skills-api'),
    path('portfolios/', PortfolioListView.as_view(), name='portfolio-list-api'),
    path('portfolios/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail-api'),
    path('contact/', ContactMessageView.as_view(), name='contact-api'),
]
