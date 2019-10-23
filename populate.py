import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Book_Project.settings')

import django
django.setup()

from Book.models import Book
from faker import Faker
from random import *
from django.contrib.auth.models import User

faker = Faker()

def populate(n):
    branch_list = ['ISE','CSE','ME','ECE','EEE','CVE']
    book_name   = ['M-2','physics','basic civil','basic electrical','mechanical',]
    for i in range(n):
        bname = faker.word(ext_word_list = book_name)
        semester = randint(1,8)
        bauthor = faker.name()
        branch = faker.word(ext_word_list = branch_list)
        user = User.objects.get(username__exact = 'piyush')
        book = Book.objects.get_or_create(buser = user,bname=bname,semester=2,bauthor=bauthor,branch='CSE')
populate(8)
