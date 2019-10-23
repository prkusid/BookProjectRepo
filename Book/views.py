from django.shortcuts import render,redirect
from Book.models import Book,UserProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime



# Create your views here.

# main home page
def main_home_page(request):
    return render(request,'main_home.html')

#home page view
def home(request):
    return render(request,'Book/home.html')

# after login home page
@login_required
def after_login_home(request):
    return render(request,'Book/after_login_home_page.html',{'login_user':request.user})


#book_list view
def book_list(request,sem,branch = None):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(bname__icontains = search)|Book.objects.filter(semester__icontains = search)
        return render(request,'Book/book_list.html',{'books':books})
    else:
        if branch:
            books = Book.objects.filter(Q(semester__contains = sem),Q(branch__icontains = branch))
        else:
            books = Book.objects.filter(semester__contains = sem)
        return render(request,'Book/book_list.html',{'books':books})

# book list after login
@login_required
def after_login_book_list(request,sem,branch=None):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(Q(bname__icontains = search),~Q(buser__exact = request.user))|Book.objects.filter(Q(semester__icontains = search),~Q(buser__exact = request.user))
        return render(request,'Book/after_login_book_list_page.html',{'books':books,'login_user':request.user})
    else:
        if branch:
            books = Book.objects.filter(Q(semester__contains = sem),~Q(buser__exact = request.user),Q(branch__icontains = branch))
        else:
            books = Book.objects.filter(Q(semester__contains = sem),~Q(buser__exact = request.user))
        return render(request,'Book/after_login_book_list_page.html',{'books':books,'login_user':request.user})

#login view
@login_required
def borrow(request,id):
    book = Book.objects.get(id = id)
    user = UserProfile.objects.get(user = book.buser)
    return render(request,'Book/book_details.html',{'book':book,'user':user,'login_user':request.user})

# views for sign up
def sign_up(request):

    if request.method == 'POST':
        uname           =   request.POST['uname']
        uemail          =   request.POST['uemail']
        uusername       =   request.POST['uusername']
        umobile         =   request.POST['umobile']
        upassword       =   request.POST['upassword']
        ucpassword      =   request.POST['ucpassword']
        uaddress1       =   request.POST['uaddress1']
        uaddress2       =   request.POST['uaddress2']

        # mobile number checking
        if (not umobile.isdigit()) or (len(umobile) != 10):
            flag_mobile = True
            return render(request,'Book/sign_up.html',{'msg':'Mobile Number must be number of 10 digits only','flag_mobile':flag_mobile})

        # password confirming
        if upassword != ucpassword:
            flag_password = True
            return render(request,'Book/sign_up.html',{'msg':'Password and Confirm Password must be same','flag_password':flag_password})

        #checking username is available or not
        try:
            available_user = User.objects.get(username__exact = uusername)
            flag_user = True
            return render(request,'Book/sign_up.html',{'msg':'Username is already registered try another','flag_user':flag_user})

        except User.DoesNotExist:
            user = User(first_name=uname,email=uemail,username=uusername,password=upassword)
            user.set_password(user.password)
            user.save()
            userprofile = UserProfile(user=user,mobile_no = umobile,address1 = uaddress1,address2 = uaddress2)
            userprofile.save()
            return HttpResponseRedirect('/accounts/login')

    else:
        return render(request,'Book/sign_up.html')


# add book views
@login_required
def add_book(request):

    if request.method == 'POST':

        bname           =  request.POST['bname']
        bsemester       =  request.POST['bsemester']
        bauthor         =  request.POST['bauthor']
        bbranch         =  request.POST['bbranch']

        try:
            bsemester = int(bsemester)
            if bsemester > 8 or bsemester < 1:
                flag_semester = True
                return render(request,'Book/add_book.html',{'msg':'semester must be a number between 1 to 8','login_user':request.user,'flag_semester':flag_semester})

            if bbranch.isdigit():
                flag_branch = True
                return render(request,'Book/add_book.html',{'msg':'branch cannot be a digit','login_user':request.user,'flag_branch':flag_branch})

            book = Book(buser=request.user,bname=bname,semester=bsemester,bauthor=bauthor,branch=bbranch)
            book.save()
            return redirect("/Book/uploaded_book")
        except ValueError:
            flag_semester = True
            return render(request,'Book/add_book.html',{'msg':'semester must be a number between 1 to 8','login_user':request.user,'flag_semester':flag_semester})

    else:
        return render(request,'Book/add_book.html',{'login_user':request.user})

# user uploaded book list views
@login_required
def user_uploaded_book(request):
    books = Book.objects.filter(buser__exact = request.user).order_by('-time')
    return render(request,'Book/user_uploaded_book.html',{'books':books,'login_user':request.user})

# view for delete the books
@login_required
def delete_book(request,id):
    book = Book.objects.get(id = id)
    book.delete()
    return redirect("/Book/uploaded_book")

# views for book Taken
@login_required
def book_taken(request,id):
    book = Book.objects.get(id = id)
    book.buser = request.user
    book.time  = datetime.now()
    book.save()
    return redirect("/Book/uploaded_book")

# views for branch after login
def branch(request,id):
    return render(request,'Book/branch.html',{'sem':id})

# views for branch after login
@login_required
def after_login_branch(request,id):
    return render(request,'Book/after_login_branch.html',{'sem':id,'login_user':request.user})
