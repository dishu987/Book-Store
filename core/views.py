from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import requests
from bs4 import BeautifulSoup
from time import sleep
from .util import *
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import RegisterationForm
from django.views import View
from django.contrib import messages
from django.utils.timezone import now,datetime

def home(request):
    saved_len=0
    recent_search=[]
    if request.user.is_authenticated:
        data1 = Favbooks.objects.filter(user=request.user)
        saved_len = len(data1)
        recent_search = RecentSearch.objects.filter(user=request.user).order_by('-id')
    if request.method=="POST":
        name = request.POST['name']
        return redirect(find, name,1)
    return render(request,"base/base.html",{"saved_len":saved_len,"recent_search":recent_search})


def find(request,name,page):
    if page<1:
        return redirect(find,name,1)
    if request.method=="POST":
        if request.POST.get("save_to_fav")=="save_to_fav":
            #  <!-- ('id','title','selling_price','discounted','description','brand','product_image',) -->
            title = request.POST['title']
            selling_price = request.POST['selling_price']
            discounted = request.POST['discounted']
            brand = request.POST['brand']
            product_image = request.POST['product_image']
            auther = request.POST['auther']
            description = request.POST['description']
            date = request.POST['date']
            rating_count = request.POST['rating_count']
            rating = request.POST['rating']
            Favbooks(user = request.user,title=title,selling_price=selling_price,discounted=discounted,description=description,brand=brand,product_image=product_image,auther=auther,date=date,rating_count=rating_count,rating=rating).save()
            return redirect(saved_books,1)
        else:
            name = request.POST['name']
            return redirect(find, name,1)
    is_valid = False
    data = get_Amazon(name)
    saved_len=0
    tot_result = len(data)
    recent_search=[]
    if request.user.is_authenticated:
        RecentSearch(user = request.user,name=name).save()
        data1 = Favbooks.objects.filter(user=request.user)
        saved_len = len(data1)
        recent_search = RecentSearch.objects.filter(user=request.user).order_by('-id')
    if len(data)>0:
        is_valid = True
    i=0
    tot_pages=len(data)/10+1
    if tot_pages<page:
        return redirect(find,name,1)
    newData = []
    for d in data:
        if i<page*10 and i>=10*(page-1):
            newData.append(d)
        i=i+1
    context = {
        "data":newData,
        "is_valid":is_valid,
        "saved_len":saved_len,
        "tot_result":tot_result,
        "page":page,
        "name":name,
        "tot_pages":tot_pages,
        "recent_search": recent_search,
    }
    return render(request,"base/search_books.html",context)
    
@login_required
def saved_books(request,page):
    if request.method=="POST":
        if request.POST.get('delete_book')=='delete_book':
            book_id = request.POST['book_id']
            c = Favbooks.objects.filter(pk=book_id)
            c.delete()
            messages.success(request,'Congrats! Deleted successfully.')
        else:
            name = request.POST['name']
            return redirect(find, name,1)
    data = Favbooks.objects.filter(user=request.user)
    recent_search = RecentSearch.objects.filter(user=request.user).order_by('-id')
    saved_len = len(data)
    is_valid = False
    if len(data)>0:
        is_valid = True

    context={
        "data":data,
        "is_valid":is_valid,
        "saved_len":saved_len,
        "recent_search":recent_search,
    }
    return render(request,"base/saved.html",context)

@login_required
def ClearRecent(request,username):
    userNow = request.user.username
    if userNow==username:
        recent_search = RecentSearch.objects.filter(user=request.user)
        recent_search.delete()
        return HttpResponse("<script>alert('Recent Cleared! Click Ok to got home');window.location.replace('/');</script>")
    else:
        print("Access Denied!")
        return HttpResponse("<script>alert('Access Denied! Click ok to go home');window.location.replace('/');</script>")
    return redirect(home)


class RegisterationView(View):
    def get(self,request):
        form = RegisterationForm()
        return render(request, 'base/registration.html',{'form':form})   
    def post(self,request):
        form = RegisterationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congrats! registered successfully.')
            form.save()
        else:
            messages.warning(request,'Oops! Some error occurred.')
        return render(request, 'base/registration.html',{'form':form})


def Error_404(request,exception):
    return render(request, 'base/404.html')
