from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import Profile, Skill, Portfolio, PortfolioImage, ContactMessage

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImage
        fields = ['image']

class PortfolioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'category', 'image', 'client', 'project_date']

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        
    def validate_email(self, value):
        """Validasi format email"""
        if '@' not in value:
            raise serializers.ValidationError("Enter a valid email address.")
        return value
        
    def validate_name(self, value):
        """Validasi nama tidak kosong dan tidak hanya spasi"""
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value.strip()
        
    def validate_message(self, value):
        """Validasi pesan minimal 5 karakter"""
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Message must be at least 5 characters long.")
        return value.strip()

class PortfolioDetailSerializer(serializers.ModelSerializer):
    gallery = PortfolioImageSerializer(many=True, required=False)

    project_url = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'category', 'image', 'client', 'project_date', 'project_url', 'description', 'gallery']
