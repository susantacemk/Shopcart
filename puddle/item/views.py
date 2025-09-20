from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Item,Category
from .forms import NewItemForms,EditItemForm

def readMore(request, pk):
    item = get_object_or_404(Item,id = pk)
    related_items = Item.objects.filter(category = item.category , is_sold = False).exclude(id=pk)[0:3] # related 3 items are shown
    context = {'item':item,'related_items':related_items}
    return render(request,'item/details.html',context)



@login_required
def new(request):
    if request.method=='POST':
        form = NewItemForms(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:readMore',pk = item.id)
    else:
        form = NewItemForms()
    context={'form':form,'title':'New Item'}
    return render(request,'item/newItem.html',context)



@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect('item:readMore', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/newItem.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request,pk):
    item = get_object_or_404(Item,id = pk , created_by = request.user)
    item.delete()
    return redirect('dashboard:my_page')

def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/browse.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })
