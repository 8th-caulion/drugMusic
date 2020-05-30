from django.shortcuts import render, redirect

# Create your views here.
def main(request):
    return render(request, 'main.html')

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
    return redirect('/')