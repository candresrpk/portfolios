from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def signup_view(request):

    context = {
        'form': UserCreationForm
    }

    if request.method == 'GET':
        return render(request, './users/signup.html', context)

    else:
        if request.POST['password1'] != request.POST['password2']:
            context['message'] = 'Passwords do not match'
            return render(request, './users/signup.html', context)
        try:

            user = User.objects.create_superuser(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            user.save()
            login(request, user)

            return redirect('hosaik:home')
        except IntegrityError:
            context['message'] = 'Username is already taken'
            return render(request, './users/signup.html', context)
        except Exception as e:
            return render(request, './users/signup.html', {'message': str(e)})


def login_view(request):

    context = {
        'form': AuthenticationForm
    }

    if request.method == 'GET':
        return render(request, './users/login.html', context)

    else:
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is None:
            context['message'] = 'Username and password do not match'
            return render(request, './users/login.html', context)
        else:
            login(request, user)
            return redirect('hosaik:home')


def logout_view(request):
    logout(request)
    return redirect('hosaik:home')
