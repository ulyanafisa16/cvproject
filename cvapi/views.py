from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Skill, Portfolio
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ProfileSerializer, SkillSerializer, PortfolioListSerializer, PortfolioDetailSerializer, ContactMessageSerializer

class ProfileView(APIView):
    def get(self, request):
        profile = Profile.objects.first()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

class SkillView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

class PortfolioListView(APIView):
    def get(self, request):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioListSerializer(portfolios, many=True)
        return Response(serializer.data)

class PortfolioDetailView(APIView):
    def get(self, request, pk):
        portfolio = Portfolio.objects.get(pk=pk)
        serializer = PortfolioDetailSerializer(portfolio)
        return Response(serializer.data)

class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Kirim email
            send_mail(
                subject=serializer.validated_data['subject'],
                message=serializer.validated_data['message'],
                from_email=serializer.validated_data['email'],
                recipient_list=['emailkamu@example.com'],  # Ganti dengan email kamu
            )
            return Response({"message": "Message sent successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)