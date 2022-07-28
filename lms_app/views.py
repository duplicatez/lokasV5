from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm  #ADMIN "CATEGORYFORM"

# Create your views here.




def index(request):  #ADMINONLLLY!!!!!!!!!!!!
    if request.method == 'POST':  #ADMINONLLLY!!!!!!!!!!!!
        add_book = BookForm(request.POST, request.FILES)  #ADMINONLLLY!!!!!!!!!!!!
        if add_book.is_valid():#ADMINONLLLY!!!!!!!!!!!!
            add_book.save()#ADMINONLLLY!!!!!!!!!!!!



        add_category = CategoryForm(request.POST)  #ADMINONLLLY!!!!!!!!!!!!
        if add_category.is_valid():  #ADMINONLLLY!!!!!!!!!!!!
            add_category.save()    #ADMINONLLLY!!!!!!!!!!!!





    context = {
        'category' : Category.objects.all(),
        'books' : Book.objects.all(),
        'form' : BookForm(),
        'formcat': CategoryForm(),  #ADMIN
    }
    return render(request, 'pages/index.html', context)


def books(request):
    context = {
        'category' : Category.objects.all(),
        'books' : Book.objects.all(),
    }
     
     

    
    return render(request, 'pages/books.html',context)


def update (request, id):                #Admin
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
            
    else:
        book_save = BookForm(instance=book_id)
    context = {
        'form':book_save,
    }
    return render(request, 'pages/update.html', context)



def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')