from django.shortcuts import render, redirect, get_object_or_404
from .schedule import getSchedule
from .models import Profile, Video
from django.core.paginator import Paginator

def categoryString(index):
    categories = ['발라드', 'R&B/소울', '인디락', '랩/힙합', '포크/어쿠스틱', '신스팝', '재즈']
    return categories[index]

def categoryChangedProfile(profile):
    profile.category = categoryString(profile.category)
    return profile

def videoLinkGenerate(video):
    video.link = "https://www.youtube.com/embed/" + str(video.link)
    return video

def dateChange(profile):
    profile.post_date = profile.post_date.strftime("%Y %b %d")
    return profile

# Create your views here.
def main(request):
    recommendedProfiles = Profile.objects.all().order_by("?")[:30]
    updatedProfiles= Profile.objects.all().order_by('-post_date')[:8]
    updatedProfiles = list(map(dateChange, updatedProfiles))
    return render(request, 'main.html', {"recommendedProfiles":recommendedProfiles, 'updatedProfiles' : updatedProfiles})

def edit(request, id):
    profile = get_object_or_404(Profile, pk=id)
    return render(request, 'edit.html', {'profile' : profile})

def update(request, id):
    profile = get_object_or_404(Profile, pk=id)
    profile.name = request.POST['name']
    profile.category = request.POST['genre']
    profile.place = request.POST['place']
    profile.line = request.POST['comment']
    profile.detail = request.POST['text']
    if request.FILES:
        profile.image = request.FILES['photo']
   
    profile.save()

    return redirect('/')


def profile(request):
    profiles = Profile.objects.all()
    paginator = Paginator(profiles, 8)
    page = request.GET.get('page')
    profiles = paginator.get_page(page)
    profiles = list(map(categoryChangedProfile, profiles))
    return render(request, 'profile.html', {"profiles":profiles})

def detailProfile(request, id):
    profile = get_object_or_404(Profile, pk=id)
    profile.category = categoryString(profile.category)
    profile.changedVideos = list(map(videoLinkGenerate, profile.videos.all()))
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

def video(request, artist_id):
    print(artist_id)
    link = request.POST.get('link')
    video = Video()
    video.link = link
    myprofile = get_object_or_404(Profile, pk=artist_id)
    print(link)
    print(myprofile)
    video.profile = myprofile
    video.save()
    return redirect('/profile/' + str(artist_id))


def schedule(request):

    schedule = getSchedule()
    print(schedule)

    return render(request, 'schedule.html')
