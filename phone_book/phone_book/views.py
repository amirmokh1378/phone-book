from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from phone_book_contacts.forms import AddFileForm


# Create your views here.


def home_view(request, **kwargs):
    add_file_form = AddFileForm()
    context = {
        'add_file_form': add_file_form,
    }

    return render(request, template_name='home.html', context=context)


@require_http_methods(["GET"])
def search_view(request):
    add_file_form = AddFileForm()
    context = {
        'add_file_form': add_file_form,
    }
    return render(request, template_name='search.html', context=context)
