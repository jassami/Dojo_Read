from django.shortcuts import render, redirect
from django.apps import apps
User = apps.get_model('login_app', 'User')
from .models import *

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context={
        'user': User.objects.get(id = request.session['user_id']),
        'latest': Review.objects.all().order_by("-created_at")[:3],
    }
    return render(request, 'dojo.html', context)


def add(request):
    Author.objects.create(name= "Stephen King")
    Author.objects.create(name= "Paulo Coelho")
    Author.objects.create(name= "Mitch Albom")
    context={
        'authors': Author.objects.all().order_by("id")[:3],
    }
    return render(request, 'add.html', context)

def add_book(request):
    this_user= User.objects.get(id= request.session['user_id'])
    if request.POST['author_list'] == "":
        book_author= Author.objects.create(name= request.POST['name'])
    else:
        book_author= Author.objects.get(id= request.POST['author_list'])
    this_book= Book.objects.create(title= request.POST['title'], user= this_user, author= book_author)
    book_review= Review.objects.create(review= request.POST['review'], rating= request.POST['rating'], user= this_user, book= this_book)
    request.session['book_id']= this_book.id
    request.session['review_id']= book_review.id
    return redirect(f'/books/{this_book.id}')

def book_info(request, book_id):
    context={
        'book': Book.objects.get(id= book_id),
        'user': User.objects.get(id= request.session['user_id'])
    }
    return render(request, 'book_info.html', context)

def delete(request, book_id, review_id):
    review= Review.objects.get(id = review_id)
    review.delete()
    return redirect(f'/books/{book_id}')

def add_review(request, book_id):
    this_book= Book.objects.get(id= book_id)
    this_user= User.objects.get(id = request.session['user_id'])
    book_review= Review.objects.create(review= request.POST['review'], rating= request.POST['rating'], user= this_user, book= this_book)
    request.session['review_id']= book_review.id
    return redirect(f'/books/{book_id}')

def users(request, user_id):
    context={
        'user': User.objects.get(id= user_id),
    }
    return render(request, 'users.html', context)






    # {% with ''|center:review.rating as range %}
    #         {% for _ in range %}
    #             <span class="material-icons">grade</span>
    #         {% endfor %}
    #         {% endwith %}