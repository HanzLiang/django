import imp
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

def page1_view(request):
    html = '<h1>这是页面page1</h1>'
    return HttpResponse(html)

def page2_view(request):
    html = '<h1>这是页面page2</h1>'
    return HttpResponse(html)

def pagen_view(request, pg):
    html = '<h1>这是页面page{}</h1>'.format(pg)
    return HttpResponse(html)

def page_calculate_view(request,n,op,m):
    # 一个小的保护
    if op not in ['add','sub','mul']:
        html = '<h1>Your op is wrong<h1>'

    if op == 'add':
        html = '<h1>{}<h1>'.format(n+m)
    if op == 'sub':
        html = '<h1>{}<h1>'.format(n-m)
    if op == 'mul':
        html = '<h1>{}<h1>'.format(n*m)
    
    return HttpResponse(html)

def page_test_request(request):
    print('request.path_info:',request.path_info)
    print('request.method:',request.method)
    print('request.querystring:',request.GET)
    return HttpResponseRedirect('/page/1')

def test_get(request):
    print(request.GET.get('a','no a'))
    return HttpResponse('ok')

# 方案1
# def test_html(request):
#     t=loader.get_template('test_html.html')
#     html=t.render()
#     return HttpResponse(html)

# 方案2
def test_html(request):
    dic={'int':88,
    'str':'hans',
    'list':['tom','jack','lily'],
    'dict':{'1':1,'2':2},
    'func':sayHi,
    'obj':Dog(),
    'script':'<script>alert(111)</script>'
    }
    return render(request,'test_html.html',dic)

def sayHi():
    return 'hahaha'

class Dog:
    name='xiaogou'
    def say(self):
        return 'wangwangwang'


def test_if_for(request):
    dic={'x':50,'lst':['apple','pear','peach']}
    return render(request,'test_if_for.html',dic)


def mycal(request):
    if request.method == 'POST':
        x=int(request.POST.get('x'))
        y=int(request.POST.get('y'))
        op=request.POST.get('op')
        res=0
        if op == 'add':
            res=x+y
        elif op == 'sub':
            res=x-y
        elif op == 'mul':
            res=x*y
        elif op == 'div':
            res=x/y
        
        return render(request,'mycal.html',locals())

    elif request.method == 'GET':
        dic={'x':1,'op':'add','y':1,'res':2}
        return render(request,'mycal.html',dic)

def base_view(request):
    return render(request,'base.html')

def music_view(request):
    return render(request,'music.html')

def sport_view(request):
    return render(request,'sport.html')

def test_url(request):
    return render(request,'test_url.html')

def test_static(request):
    return render(request, 'test_static.html')