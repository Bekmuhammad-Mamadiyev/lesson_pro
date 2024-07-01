from django.shortcuts import render
from kompaniya.models import Maqola,Resume,BlogSetting


def homepage(request):
    blog = BlogSetting.objects.all()
    context = {
        "blog":blog
    }
    return render(request,'home.html',context)

def blogspage(request):
    maqola = Maqola.objects.all()
    context = {
            'maqola': maqola
    }
    return render(request,'blogs.html',context)

def resumepage(request):
    resume = Resume.objects.all()
    context={
        "resume":resume
    }
    return render(request,'resume.html',context)