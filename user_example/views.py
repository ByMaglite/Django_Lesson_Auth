from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home_view(request):
    return render(request, 'user_example/home.html')

@login_required
def special(request):
    return render(request, 'user_example/special.html')


def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=password)
            
            login(request, user)
            
            return redirect('home')
        
    
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/register.html", context)


def password_change(request):
    
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = UserChangeForm()
    context = {
        'form': form
    }
    return render(request, "registration/password_change.html", context)