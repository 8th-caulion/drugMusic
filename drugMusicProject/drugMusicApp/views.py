from django.shortcuts import render, redirect
from .schedule import getSchedule
from .models import Profile, Video

# Create your views here.
def main(request):
    profiles = Profile.objects.all
    return render(request, 'main.html', {"profiles":profiles})

def profile(request):
    return render(request, 'profile.html')

def profileNew(request):

    return render(request, 'form.html')

def profileSave(request):
    name = request.POST['name']
    genre = request.POST['genre']
    place = request.POST['place']
    comment = request.POST['comment']
    text = request.POST['text']
    img = request.FILES['photo']
    print(name, genre, place, comment, text, img)

    profile = Profile()
    profile.name = name
    profile.category = genre
    profile.place = place
    profile.line = comment
    profile.detail = text
    profile.image = img

    profile.save()

    return redirect('/')

def schedule(request):

    schedule = getSchedule()
    print(schedule)

    return render(request, 'schedule.html')
