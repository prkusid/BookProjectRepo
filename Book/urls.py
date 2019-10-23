"""Book_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Book import views


urlpatterns = [
    path('', views.home),
    path('borrow/<int:id>', views.borrow),                                 # url for book borrow
    path('sign_up', views.sign_up),                                        # url for sign up
    path('book_list/<int:sem>', views.book_list),                          # url for listing of available books
    path('book_list/<int:sem>/<branch>', views.book_list),                 # url for sem1 and sem2 book list
    path('add_book', views.add_book,),                                     # url for add book
    path('uploaded_book', views.user_uploaded_book,),                      # url for user uploaded book list
    path('delete_book/<int:id>', views.delete_book),                       # url for delete the book
    path('book_taken/<int:id>', views.book_taken),                         # url for book taken view
    path('branch/<int:id>', views.branch),

    path('after_login_branch/<int:id>', views.after_login_branch),          # url for branch view after login
    path('after_login_home', views.after_login_home),                       # url for after login
    path('after_login_book_list/<int:sem>', views.after_login_book_list),   # url for sem1 and sem2 book list after login
    path('after_login_book_list/<int:sem>/<branch>', views.after_login_book_list),   # url for book list afetr login
]
