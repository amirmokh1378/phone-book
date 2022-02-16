"""phone_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

app_name = 'phone_book_contacts'
from .views import *

urlpatterns = [
    path('delete-contact', delete_contact_component_view, name='delete'),
    path('show-contact', show_contact_component_view, name='show'),
    path('add-contact-by-form', add_contact_by_form_component_view, name='add_form'),
    path('add-contact-by-file', add_contact_by_file_component_view, name='add_file'),
    path('search-contact', search_contact_component_view, name='search'),
]
