from django import forms
from .models import Profile, Skill, Portfolio, PortfolioImage, ContactMessage

# ---------------- Profile Form ----------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'profession', 'intro', 'photo',
            'email', 'phone', 'address', 'birth_date',
            'degree', 'freelance'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'freelance': forms.TextInput(attrs={'class': 'form-control'}),
        }

# ---------------- Skill Form ----------------
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percentage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'percentage': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
        }

# ---------------- Portfolio Form ----------------
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'category', 'image', 'client', 'project_date', 'project_url', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'client': forms.TextInput(attrs={'class': 'form-control'}),
            'project_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'project_url': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

# ---------------- Portfolio Image Form ----------------
class PortfolioImageForm(forms.ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ['portfolio', 'image']
        widgets = {
            'portfolio': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# ---------------- Contact Message Form ----------------
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
