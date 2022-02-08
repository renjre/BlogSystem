from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

def index(request):
    data = Book.objects.all()
    context = {'data': data}
    return render(request, "index.html", context)


def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        # import pdb; pdb.set_trace()

        User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname)
        return redirect("home")

    return render(request, "signup.html")        

def user_login(request):
    if request.method == "POST":
        user = request.POST['user']
        password = request.POST['password']
        # import pdb; pdb.set_trace()
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Username or password is not matched")
    else:
        return render(request, "login.html")

        
def user_logout(request):
    logout(request)
    return redirect("home")



@login_required(login_url='login')
def book(request):
    if request.method == "POST" and request.user.is_authenticated:
        # import pdb;pdb.set_trace()
        title = request.POST['title']
        desc = request.POST['desc']
        image = request.FILES.get('img')

        b = Book.objects.create(create_by= request.user, book_title=title, book_desc=desc, book_img = image)
        return redirect("home")
    else:
        return render(request, 'createpost.html')

    return render(request, 'createpost.html')

def seebook(request, id):
    global book_details
    book_details = Book.objects.filter(id=id)
    global a
    a = Book.objects.get(id=id)
    global comm
    comm = Comment.objects.all().filter(bookid_id=a.id)
    context = {'book': book_details, 'comment': comm}

    # import pdb;pdb.set_trace()
    # create comment 
    ##########################
    
    if request.method == "POST" and request.user.is_authenticated:
        if request.POST.get('like') != "":
            l = LikeBook.objects.create(like_by=request.user, bookid_id=a.id, like=True)


        comment= request.POST.get('comment')
        context = {'error': "please provide comment"}
        if not comment:
            return render(request, "seebook.html", context)

        c = Comment.objects.create(comment_by=request.user, bookid_id=a.id, comment=comment)
        return HttpResponseRedirect("/book/%i" %id)

    ##########################
    
    else:
        return render(request, "seebook.html", context)
    
def delete_comment(request, id):
     if request.method == "GET":
        deletecomm = Comment.objects.filter(pk=id)
        deletecomm.delete()
        # return HttpResponse("Comment deleted")
        # return redirect("seebook")
        return HttpResponseRedirect("/book/%i" %a.id)

def update_comment(request, id):
    updatecomm = Comment.objects.filter(pk=id)
    if request.method == "POST":
        updatecomm = Comment.objects.get(pk=id)
        updatecomm.comment = request.POST.get('comment')
        updatecomm.save()
        return HttpResponseRedirect("/book/%i" %a.id)
    book_details
    cont = {'book': book_details, 'comment': updatecomm}
    return render(request, 'updatecomm.html', cont)


def likebook(request):
    if request.method == "POST":
        like = request.POST.get('like')
        l = LikeBook.objects.create(like_by=request.user, bookid_id=a.id, like=like)






# updatedata
def delete_book(request,id):
    if request.method == "POST":
        delete_book = Book.objects.filter(pk=id)
        delete_book.delete()
        return redirect("home")
        # return HttpResponse("Book deleted")




def update_book(request,id):
    data = Book.objects.get(id=id)
    context = {'book': data}
    # import pdb;pdb.set_trace()
    if request.user.id == Book.objects.get(id=id).create_by_id:
        if request.method == "POST":
            data.book_title = request.POST.get('title')
            data.book_desc = request.POST.get('desc')
            data.book_img = request.FILES.get('newimg') 
            data.save()
            return redirect("home")
        else:
            return render(request, 'updatebook.html',context)
    else:
        return HttpResponse("You are not authenticate for doing this")
    return render(request, 'updatebook.html',context)


###########################################################


# Comment view``
