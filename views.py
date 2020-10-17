from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    if request.method == "POST":
    title = request.POST['title']
    desc = request.POST['desc']
    print(title,desc)
    return render(request, 'index.html')
def Notes(request):
    return render(request, 'note.html')



