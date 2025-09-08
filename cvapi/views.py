from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Skill, Portfolio,ContactMessage
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import send_mail
from .serializers import ProfileSerializer, SkillSerializer, PortfolioListSerializer, PortfolioDetailSerializer, ContactMessageSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Profile
from .serializers import ProfileSerializer

class ProfileView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    # GET /api/profiles/  -> list semua profile
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    # POST /api/profiles/ -> buat profile baru
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    # GET /api/profiles/<pk>/ -> detail profile
    def get(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    # PUT /api/profiles/<pk>/ -> update profile
    def put(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE /api/profiles/<pk>/ -> hapus profile
    def delete(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SkillView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SkillDetailView(APIView):
    def get(self, request, pk):
        try:
            skill = Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            skill = Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            skill = Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# views.py

class PortfolioListView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioListSerializer(portfolios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PortfolioDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PortfolioDetailView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except Portfolio.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PortfolioDetailSerializer(portfolio)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except Portfolio.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PortfolioDetailSerializer(portfolio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except Portfolio.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContactMessageView(APIView):
    def get(self, request):
        messages = ContactMessage.objects.all()
        serializer = ContactMessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                subject=serializer.validated_data['subject'],
                message=serializer.validated_data['message'],
                from_email=serializer.validated_data['email'],
                recipient_list=['emailkamu@example.com'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactMessageDetailView(APIView):
    def delete(self, request, pk):
        try:
            msg = ContactMessage.objects.get(pk=pk)
        except ContactMessage.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        msg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
