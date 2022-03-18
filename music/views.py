from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from music.models import Book


# Create your views here.

def index_view(request):
    # return HttpResponse("这是音乐频道")
    # 当内外层templates都存在时
    # django优先在外层查找，外层没有暗战INSTALLED_APP应用顺序查找
    # return render(request,'index.html')
    
    # 解决方法：
    # 在应用下的templates文件夹下创建一个和应用名称相同的文件夹，
    # 将之前的index.html移动到该文件夹下：
    return render(request,'music/index.html')

def all_book(request):
    
    all_book = Book.objects.all().filter(is_active=True)
    return render(request, 'music/all_book.html',locals())

def book_update(request, id):
    try:
        update_book = Book.objects.get(id=id)
    except Exception as e:
        print('--update book error is %s' % (e))
        HttpResponse("--This book is not existed")


    if request.method == 'GET':

        return render(request, 'music/update.html', locals())
    elif request.method == 'POST':


        update_book.price = request.POST.get('price')

        update_book.market_price = request.POST.get('market_price')

        update_book.save()


        return HttpResponseRedirect('/music/all_book')

def book_delete(request):
        id = request.GET.get('id')
        print(id)
        if not id:
            HttpResponse("--请求异常")
        try:
            b = Book.objects.get(id = id, is_active=True)
            b.is_active=False
            b.save()
        except:
            HttpResponse("--This book is not existed")
        
        return HttpResponseRedirect('/music/all_book')


