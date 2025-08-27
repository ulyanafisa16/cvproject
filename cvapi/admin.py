from django.contrib import admin
from .models import Profile, Skill, Portfolio, PortfolioImage, ContactMessage

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Portfolio)
admin.site.register(PortfolioImage)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
