"""WSBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login.views import default_EnterCredentials_view, noValidCredentials_view
from items.views import item_detail_view, item_create_view, item_edit_view, item_search_view, item_list_view, item_delete_view

# Debug
from django.conf import settings
from django.conf.urls.static import static

#Urls for all pages and their respective views.
urlpatterns = [
    # Auth
    path('accounts/', include('django.contrib.auth.urls')),

    # AdminPanel
    path('admin/', admin.site.urls),

    # DefaultPage
    path("", default_EnterCredentials_view, name="defaultSite"),
    path("login/InvalidCredentialsOrSession", noValidCredentials_view, name="invalidCreds"),

    # Items
    path("item/list/", item_list_view, name="item-list"),
    path("item/list/<int:sortBy>/", item_list_view, name="item-list-sorted"),
    path("item/detail/<int:my_id>/", item_detail_view, name="item-detail"),
    path("item/create/", item_create_view, name="item-create"),
    path("item/edit/<int:my_id>/", item_edit_view, name="item-edit"),
    path("item/delete/<int:my_id>/", item_delete_view, name="item-delete"),
    path("item/search/", item_search_view, name="item-search")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# Initial Setup
""" Code input here will get run exactly once at Programm start """