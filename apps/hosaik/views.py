from django.shortcuts import render

# Create your views here.


def home_view(request):
    username = request.user.username
    context = {
        'username': username
    }
    return render(request, './hosaik/home.html', context)
