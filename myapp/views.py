from django.shortcuts import render

from .forms import IMAGEform
from .models import IMAGE
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = IMAGEform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    form = IMAGEform()
    img = IMAGE.objects.all()
    return render(request, 'myapp/home.html', {'img':img,"form":form})