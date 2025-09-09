from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout
from cvapi.models import Profile, Skill, Portfolio, PortfolioImage, ContactMessage
from cvapi.forms import ProfileForm, SkillForm, PortfolioForm, PortfolioImageForm, ContactMessageForm

# ---------------- HOME & LOGIN ----------------
@login_required(login_url='login')
def index(request):
    print("Profile count:", Profile.objects.count())
    print("Skill count:", Skill.objects.count())
    context = {
        'profile_count': Profile.objects.count(),
        'skill_count': Skill.objects.count(),
        'portfolio_count': Portfolio.objects.count(),
        'message_count': ContactMessage.objects.count(),
    }
    return render(request, 'frontend/dashboard.html', context)

@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'frontend/login.html', {'error': 'Username atau password salah'})
    return render(request, 'frontend/login.html')

@never_cache
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

@never_cache
@login_required(login_url='login')
def dashboard(request):
    if request.user.username == 'userdashboard':
        # Dashboard untuk user biasa
        context = {
            'profile_count': Profile.objects.count(),
            'skill_count': Skill.objects.count(),
            'portfolio_count': Portfolio.objects.count(),
            'message_count': ContactMessage.objects.count(),
        }
        return render(request, 'frontend/dashboard.html', context)
    elif request.user.is_staff:
        # Dashboard untuk admin
        context = {
            'profile_count': Profile.objects.count(),
            'skill_count': Skill.objects.count(),
            'portfolio_count': Portfolio.objects.count(),
            'message_count': ContactMessage.objects.count(),
        }
        return render(request, 'frontend/dashboard.html', context)
    else:
        # User lain tidak punya akses
        return redirect('login')
# ---------------- PROFILE CRUD ----------------
@login_required(login_url='login')
def profile_list(request):
    if request.user.username == 'userdashboard':
        return redirect('dashboard') 
    profiles = Profile.objects.all()
    return render(request, 'frontend/profiles/list.html', {'profiles': profiles})

@login_required(login_url='login')
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'frontend/profiles/form.html', {'form': form})

@login_required(login_url='login')
def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'frontend/profiles/form.html', {'form': form, 'profile': profile})

@login_required(login_url='login')
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'frontend/profiles/delete.html', {'profile': profile})

# ---------------- SKILL CRUD ----------------
@login_required(login_url='login')
def skill_list(request):
    if request.user.username == 'userdashboard':
        return redirect('dashboard') 
    skills = Skill.objects.all()
    return render(request, 'frontend/skills/list.html', {'skills': skills})

@login_required(login_url='login')
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'frontend/skills/form.html', {'form': form})

@login_required(login_url='login')
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'frontend/skills/form.html', {'form': form})

@login_required(login_url='login')
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')
    return render(request, 'frontend/skills/delete.html', {'skill': skill})

# ---------------- PORTFOLIO CRUD ----------------
@login_required(login_url='login')
def portfolio_list(request):
    if request.user.username == 'userdashboard':
        return redirect('dashboard') 
    portfolios = Portfolio.objects.all()
    return render(request, 'frontend/portfolios/list.html', {'portfolios': portfolios})

@login_required(login_url='login')
def portfolio_create(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioForm()
    return render(request, 'frontend/portfolios/form.html', {'form': form})

@login_required(login_url='login')
def portfolio_edit(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'frontend/portfolios/form.html', {'form': form})

@login_required(login_url='login')
def portfolio_delete(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('portfolio_list')
    return render(request, 'frontend/portfolios/delete.html', {'portfolio': portfolio})

# ---------------- PORTFOLIO IMAGE CRUD ----------------
@login_required(login_url='login')
def portfolio_image_list(request):
    if request.user.username == 'userdashboard':
        return redirect('dashboard') 
    images = PortfolioImage.objects.all()
    return render(request, 'frontend/portfolio_images/list.html', {'images': images})

@login_required(login_url='login')
def portfolio_image_create(request):
    if request.method == 'POST':
        form = PortfolioImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio_image_list')
    else:
        form = PortfolioImageForm()
    return render(request, 'frontend/portfolio_images/form.html', {'form': form})

@login_required(login_url='login')
def portfolio_image_edit(request, pk):
    image = get_object_or_404(PortfolioImage, pk=pk)
    if request.method == 'POST':
        form = PortfolioImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('portfolio_image_list')
    else:
        form = PortfolioImageForm(instance=image)
    return render(request, 'frontend/portfolio_images/form.html', {'form': form})

@login_required(login_url='login')
def portfolio_image_delete(request, pk):
    image = get_object_or_404(PortfolioImage, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('portfolio_image_list')
    return render(request, 'frontend/portfolio_images/delete.html', {'image': image})

# ---------------- CONTACT MESSAGE ----------------
@login_required(login_url='login')
def message_list(request):
    if request.user.username == 'userdashboard':
        return redirect('dashboard') 
    messages = ContactMessage.objects.all()
    return render(request, 'frontend/messages/list.html', {'messages': messages})

@login_required(login_url='login')
def message_detail(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    return render(request, 'frontend/messages/detail.html', {'message': message})

@login_required(login_url='login')
def message_delete(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('message_list')
    return render(request, 'frontend/messages/delete.html', {'message': message})

