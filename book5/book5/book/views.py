from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo
# Create your views here.
def index(request):
    books=BookInfo.objects.all()
    for book in books:
        print(book)
    context={
        'books':books
    }
    reslut=10/10
    return render(request,'index.html',context)
    return HttpResponse('-----------------')