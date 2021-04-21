from django.shortcuts import render
from items.views import item_list_view

# Create your views here.
def home_view(request, *args, **kwargs):
    return item_list_view(request)

"""This view is currently not used, could be useful for future implementations of basic sites like contact etc..."""