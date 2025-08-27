from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    intro = models.TextField()
    photo = models.ImageField(upload_to='profile/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    birth_date = models.DateField()
    degree = models.CharField(max_length=100)
    freelance = models.CharField(max_length=50)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    client = models.CharField(max_length=100, blank=True, null=True)
    project_date = models.DateField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/gallery/')


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
