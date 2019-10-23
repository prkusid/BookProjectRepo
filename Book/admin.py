from django.contrib import admin
from Book.models import Book,UserProfile

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['buser','bname','semester','bauthor','book_available','branch','time']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','mobile_no','address1','address2']

admin.site.register(Book,BookAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
