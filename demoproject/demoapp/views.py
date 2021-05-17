from django.http import HttpResponse
from django.shortcuts import render,redirect
from.models import shops
from.forms import ModeForm
# Create your views here.





def shop(request):
    product=shops.objects.all()
    return render(request,"home.html",{'products':product})

def detail(request,book_id):
    apple=shops.objects.get(id=book_id)
    return render(request,"detail.html",{'product':apple})

def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        img=request.FILES['img']
        s=shops(name=name,desc=desc,price=price,img=img)
        s.save()
        print("added")
    return render(request,"add_product.html")

def update(request,id):
    obj = shops.objects.get(id=id)
    form = ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})

def delete(request,id):
    if request.method=="POST":
        obj=shops.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')