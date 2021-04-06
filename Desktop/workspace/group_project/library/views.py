from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from library.models import Genre, Book, Bookpage
from django.contrib.auth.models import User
import json
from validate_email import validate_email
from library.forms import UserForm, ReviewForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView
from library.models import Book, Review
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.db.models import Avg

def index(request):

    genre_list = Genre.objects.all()
    context_dict = {}
    context_dict['genres'] = genre_list
    return render(request, 'library/index.html', context=context_dict) 

def show_genre(request, genre_name_slug):

    context_dict = {}
    
    try:
        genre = Genre.objects.get(slug=genre_name_slug)
        books = Book.objects.filter(genre=genre)

        context_dict['books'] = books
        context_dict['genre'] = genre

    except Genre.DoesNotExist:
        context_dict['genre'] = None
        context_dict['books'] = None

    return render(request, 'library/genre.html', context=context_dict)



def About(request):

    return render(request, 'library/about.html')


def LogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('library:index'))
            else:
                return HttpResponse("Your Waterstones account is not active.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'library/LogIn.html')



#username validation using json
def validateUserName(request):
    data=json.loads(request.body)
    username=data['username']
    
    # check that string contains alphaneumericals and numbers
    if not str(username).isalnum():
        return JsonResponse({'username_error': 'username should only contain alphaneumerical letters and numbers, no spaces allowed.'}, status=400)   
    return JsonResponse({'username_valid': True})
    # check of username already exists
    if User.objects.filter(username=username).exists():
        return JsonResponse({'username_error': 'username already exists. Please try another one.'}, status=409)   
    return JsonResponse({'username_valid': True})

#Email validation usin json and the validate-email library
def validateEmail(request):
    data=json.loads(request.body)
    email=data['email']
    
    # check that email is correct
    if not validate_email(email):
        return JsonResponse({'email_error': 'Email is invalid, please try again'}, status=400)   
    # check of email already exists
    if User.objects.filter(email=email).exists():
        return JsonResponse({'email_errir': 'email already exists. Please try another one.'}, status=409)   
    return JsonResponse({'email_valid': True})

    

def Register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors,)
    else:
        user_form = UserForm()
    return render(request,
    'library/Register.html',
    context = {'user_form': user_form,
    'registered': registered})

def BookPage(request):

    return render(request, 'library/bookpage.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('library:index'))

def detail(request, id):
    book = Book.objects.get(id = id)
    reviews = Review.objects.filter(book = id)
    is_favorite = False    
    if book.favourites.filter(id = request.user.id).exists():
        is_favorite= True

    context_dict = {
        "book": book,
        "reviews": reviews,
        "is_favorite": is_favorite
    }
    return render(request, 'library/BookPage.html', context=context_dict)


def Bookp(request, genre_name_slug):
    context_dict = {}
    
    try:
        genre = Genre.objects.get(slug=genre_name_slug)
        books = Book.objects.filter(genre=genre)
        bookpage = Bookpage.objects.all
        
        context_dict['books'] = books
        context_dict['genre'] = genre
        context_dict['bookpage'] = bookpage

    except Genre.DoesNotExist:
        context_dict['genre'] = None
        context_dict['books'] = None
        context_dict['bookpage'] = None

    return render(request, 'library/Bookp.html',context=context_dict)

def add_review(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                reviewdata = form.save(commit=False)
                reviewdata.comment = request.POST["comment"]
                reviewdata.rating = request.POST["rating"]
                reviewdata.user = request.user
                reviewdata.book = book
                reviewdata.save()
                return redirect("library:detail", id)
        else:
            form = ReviewForm()
        return render(request, 'library/bookp.html', {"form": form})
    else:
        return redirect("library:login")

def Favourites_List(request):
    user = request.user
    favourite_book = user.favorite.all()
    context_dict = {
        'favourite_book': favourite_book,
    }
    return render(request, 'library/Favorites.html', context = context_dict)

@ login_required
def Favourites(request, id):
    book = Book.objects.get(id = id)
    if book.favourites.filter(id=request.user.id).exists():
        book.favourites.remove(request.user)
    else:
        book.favourites.add(request.user)
    return redirect("library:detail", id)



