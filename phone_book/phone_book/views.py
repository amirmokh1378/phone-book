from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods


# Create your views here.



def home_view(request):
    context = {

    }

    print('edsrewsrewre')

    return render(request, template_name='home.html', context=context)


@require_http_methods(["GET"])
def search_view(request):
    context = {
    }
    print('edsrewsrewre')

    return render(request, template_name='search.html', context=context)

