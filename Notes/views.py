from django.shortcuts import render

# Create your views here.

def notes_home(request):
    return render(request,'Notes/notes_home.html')
