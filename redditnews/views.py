from django.contrib.auth.backends import UserModel
import datetime
from redditnews.models import Post
from django.contrib.auth.forms import AuthenticationForm
from redditnews.forms import SignUpForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.timezone import utc
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login')  
def index(request):
    posts = Post.objects.order_by('-votes_total')
    return render(request, 'index.html', {'posts':posts})


# def profile(request):
#     posts = Post.objects.order_by('-votes_total')
#     return render(request, 'index.html', {'posts':posts})


def register(request):
    if request.method=="POST":
        form=SignUpForm(request.POST) 
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           user_password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=user_password)
           login(request, user)
        return redirect('login')
    else:
        form= SignUpForm()
    return render(request, 'registration/registration_form.html', {"form":form}) 

def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'http://' + request.POST['url']
            post.pub_date = datetime.datetime.utcnow().replace(tzinfo=utc)
            post.author = request.user
            post.save()
            return redirect('index')
        else:
            return render(request, 'posts/create.html', {'error': 'Error: You need a title and URL to post!'})
    else:
        return render(request, 'posts/create.html')


def profileview(request, fk):
    posts = Post.objects.filter(author__id=fk).order_by('-votes_total')
    author = User.objects.get(pk=fk)
    return render(request, 'posts/profile.html', {'posts':posts, 'author':author} )



    