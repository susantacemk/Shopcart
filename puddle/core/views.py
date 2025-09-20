from django.shortcuts import render,redirect
from django.contrib.auth import logout
from item.models import Category,Item
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:8]
    categories = Category.objects.all()
    context ={
        'items':items,
        'categories':categories
    }
    return render(request,'core/index.html',context)


def contact(request):
    return render(request,'core/contact.html')


def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
    context={'form':form}
    return render(request,'core/signup.html',context)


def logout_view(request):
    logout(request)
    return redirect('core:login')