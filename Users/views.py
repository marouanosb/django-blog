from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #save user into db
            username = form.cleaned_data.get('username')
            #show a success message
            messages.success(request, f'Thanks you {username} for registering!')
            return redirect('homepage')

            
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})