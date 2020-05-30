from django.shortcuts import render, redirect, get_object_or_404
from .schedule import getSchedule
from .models import Profile, Video

# Create your views here.
def main(request):
    profiles = Profile.objects.all
    return render(request, 'main.html', {"profiles":profiles})

def profile(request):
    return render(request, 'profile.html')

def detailProfile(request, id):
    profile = get_object_or_404(Profile, pk=id)
    categories = ['발라드', 'R&B/소울', '인디락', '랩/힙합', '포크/어쿠스틱', '신스팝', '재즈']
    profile.category = categories[profile.category]
    return render(request, 'profileDetail.html', {'profile' : profile})

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
