from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
posts=[{'author':'coreyMS',
       'title':"Blog post1",
       'content':"First post content",
       "date_posted":"october 23 2018"
        },
        {'author':'Srinivas',
       'title':"Blog post2",
       'content':"Second post content",
       "date_posted":"october 24 2018"}
              ]

def home(request):
    context={'posts':posts}
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})