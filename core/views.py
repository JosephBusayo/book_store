from django.shortcuts import render, redirect
from .models import book
from .forms import BookForm



def index(request):
    books = book.objects.all()
    return render(request, "index.html", {'books':books})


def more_detail(request, pk):
    books = book.objects.get(id=pk)
    return render(request, "moreDetails.html", {'books':books})


def add_book(request):
    #This view is meeting two ends depending on the request method
    if request.method == 'POST':
        my_form = BookForm(request.POST)
        if my_form.is_valid(): #if the info entered by user
            my_form.save()
            return redirect('/') #goes back to homepage

    my_form = BookForm() #this block works as else ie when request is GET
    return render(request, 'addBook.html', {'my_form':my_form})


def update_book(request, pk):
    to_update = book.objects.get(id=pk) #Knows which book to update depending on the data id
    my_form = BookForm(instance=to_update) #pre filling form

    if request.method == 'POST':
        my_form = BookForm(request.POST, instance=to_update) #giving it same id(to_update var) so as to aviod creating a new item
        if my_form.is_valid():
            my_form.save()
            return redirect('/')

    #update_book uses same html page as add_book, the difference being that it is pre filled
    return render(request, 'addBook.html', {'my_form':my_form})


def delete_book(request, pk):
    to_delete = book.objects.get(id=pk) #gets item to be delete based on its id

    if request.method == "POST":
        to_delete.delete()
        return redirect("/")

    return render(request, 'delete.html')
