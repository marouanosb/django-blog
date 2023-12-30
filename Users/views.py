from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
    if request.method == 'POST':
        # instance = request.user - to populate user update form with current user info
        u_form = UserUpdateForm(request.POST, instance = request.user)
        # instance = request.user.profile - to populate user update form with current user profile info
        # request.FILES to get the img file in the request
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Updated successfully.")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
    'u_form' : u_form,
    'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)