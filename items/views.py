from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from items.gl import ITEM_INDEX
from .forms import ItemAddForm, ItemEditForm
from PIL import Image
# Create your views here.

def item_detail_view(request, my_id): #Dynamic Approach
    if not request.user.is_authenticated:
        return redirect("defaultSite")
    obj = get_object_or_404(Item, id=my_id)
    values = []
    for field in Item._meta.fields:
       values.append([field.verbose_name, field.value_from_object(obj), field.name])
    context = {
        "fields": values
    }
    return render(request, "item/detail.html", context)


def item_create_view(request):
    if not request.user.is_authenticated:
        return redirect("defaultSite")
    if request.method == 'POST':
        form = ItemAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ItemAddForm()
    else: form = ItemAddForm()
    context = {
        "form": form
    }
    return render(request, "item/create.html", context)


def item_list_view(request):
    context = {
        "searchQuery": None,
        "category": "newest"
    }
    if not request.user.is_authenticated:
        return redirect("defaultSite")
    queryset = Item.objects.all() # All Items
    objList = list(queryset)
    if request.method == "GET":
        if request.GET.get("search") is not None and request.GET.get("search") != "":
            searchQuery = request.GET.get("search")
            context["searchQuery"] = searchQuery
            objList = SearchAllCategories(searchQuery)
        if request.GET.get("sortBy") is not None:
            objList = sortCats(objList=objList, sortBy=request.GET.get("sortBy"))
            context["category"] = request.GET.get("sortBy")
            print(context["category"])
    context["object_list"] = objList
    return render(request, "item/list.html", context)


def item_edit_view(request, my_id):
    if not request.user.is_authenticated:
        return redirect("defaultSite")
    obj = get_object_or_404(Item, id=my_id)
    if request.method == "POST":
        form = ItemEditForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(to=obj.get_absolute_url())
    else:
        form = ItemEditForm(instance=obj)
    context = {
        "my_id": my_id,
        "form": form
    }
    return render(request, "item/edit.html", context)


def item_search_view(request):
    return item_list_view(request)

def item_delete_view(request, my_id):
    Item.objects.filter(id=my_id).delete()
    return redirect(to="item-list")

"""
    This Website was designed for a very special use case.
    If you want to implement own/other Categories Change the content below respectively.
"""


def SearchAllCategories(userInput):
    ls = []
    for query in Item.objects.filter(name__icontains=userInput):
        ls.append(query)
    for query in Item.objects.filter(artist__icontains=userInput):
        ls.append(query)
    for query in Item.objects.filter(quantity__icontains=userInput):
        ls.append(query)
    for query in Item.objects.filter(year__icontains=userInput):
        ls.append(query)
    for query in Item.objects.filter(kindOf__icontains=userInput):
        ls.append(query)
    for query in Item.objects.filter(description__icontains=userInput):
        ls.append(query)
    for query in Item.objects.filter(glashuette__icontains=userInput):
        ls.append(query)
    for query in Item.objects.filter(color__icontains=userInput):
        ls.append(query)
    return list(dict.fromkeys(ls))

"""
    This Website was designed for a very special use case.
    If you want to implement own/other Categories Change the content below respectively.
"""


def sortCats(objList, sortBy="default"):
    if sortBy == "newest" or sortBy == "default":
        objList.sort(key=Item.getID)
        objList.reverse()
    elif sortBy == "oldest":
        objList.sort(key=Item.getID)
    elif sortBy == "nameAcs":
        objList.sort(key=Item._meta.fields[ITEM_INDEX.get("name")].value_to_string, reverse=True)
    elif sortBy == "nameDcs":
        objList.sort(key=Item._meta.fields[ITEM_INDEX.get("name")].value_to_string)
    elif sortBy == "artistAcs":
        objList.sort(key=Item._meta.fields[ITEM_INDEX.get("artist")].value_to_string, reverse=True)
    elif sortBy == "artistDcs":
        objList.sort(key=Item._meta.fields[ITEM_INDEX.get("artist")].value_to_string)
    elif sortBy == "yearAcs":
        objList.sort(key=Item._meta.fields[ITEM_INDEX.get("year")].value_to_string, reverse=True)
    elif sortBy == "yearDcs":
        objList.sort(key=Item._meta.fields[ITEM_INDEX.get("year")].value_to_string)

    return objList
