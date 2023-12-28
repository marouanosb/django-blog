from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #save user into db
            #show a success message
            messages.success(request, f'You can now login.')
            #send the username to the session
            request.session['username'] = form.cleaned_data.get('username')
            return redirect('login')

            
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required #authification required to access profile
def profile(request):
    return render(request, 'users/profile.html')