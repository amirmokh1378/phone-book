from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.http import require_http_methods
from .forms import AddForm, AddFileForm
from phone_book_contacts.models import Contact
from phone_book_accounts.models import AnonymousAccount
from sqlalchemy import create_engine
from django.http import HttpResponse
import pandas as pd
from phone_book import settings
from phone_book_tools.tools import get_equal_items_list_one_in_list_tow


# Create your views here.



user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']

database_url = 'mysql://{user}:{password}@localhost:3306/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name,
)
engine = create_engine(database_url, echo=False)


def show_contact_component_view(request):
    username = request.COOKIES.get('username')
    anonymous_account = AnonymousAccount.objects.filter(username=username).first()
    contact_qu = Contact.objects.filter(anonymous_account=anonymous_account)

    context = {
        'contact_qu': contact_qu
    }
    return render(request, template_name='contact/show_contact_component.html', context=context)


def search_contact_component_view(request):
    kwargs = dict()
    kwargs['name'] = request.GET.get('name') or ''
    kwargs['family'] = request.GET.get('family') or ''
    kwargs['email'] = request.GET.get('email') or ''
    kwargs['phone'] = request.GET.get('phone') or ''
    kwargs['num_company_or_home'] = request.GET.get('num') or ''
    kwargs['address'] = request.GET.get('address') or ''
    username = request.COOKIES.get('username') or ''
    anonymous_account = AnonymousAccount.objects.filter(username=username).first()
    contact_qu = Contact.objects.search(anonymous_account, **kwargs)
    print('search_contact_component_view: ', request.GET, '  ', contact_qu, ' ', kwargs)

    context = {
        'contact_qu': contact_qu
    }
    return render(request, template_name='contact/search_contact_component.html', context=context)


# class SearchView(TemplateView):
#     template_name = 'search.html'


def delete_contact_component_view(request):
    print(request.POST)
    username = request.COOKIES.get('username')
    anonymous_account = AnonymousAccount.objects.filter(username=username).first()
    list_pk = request.POST.getlist('PK')
    user_info = anonymous_account.contact_set.all()
    for pk in list_pk:
        user_info.filter(pk=pk).delete()

    return HttpResponse('the action delete is completely successed')


@xframe_options_exempt
def add_contact_by_form_component_view(request):
    add_form = AddForm(request.POST or None, request.FILES or None)

    if add_form.is_valid():
        print("request.FILES['file']: ", request.FILES)
        username = request.COOKIES.get('username')
        anonymous_account = AnonymousAccount.objects.filter(username=username).first()
        add_form.save(anonymous_account)

    context = {
        'add_form': add_form
    }
    return render(request, template_name='contact/add_contact_by_form_component.html', context=context)


def add_contact_by_file_component_view(request):
    add_file_form = AddFileForm(request.POST or None, request.FILES or None)
    context = {
        'add_file_form': add_file_form,
    }

    # if add_file_form.is_valid():
    #     try:
    #         df = pd.read_excel(add_file_form.files['file'])
    #         username = request.COOKIES.get('username')
    #         anonymous_account = AnonymousAccount.objects.filter(username=username).first()
    #         df['anonymous_account_id'] = anonymous_account.id
    #         print(df)
    #         df.to_sql(Contact._meta.db_table, con=engine, if_exists='append', index_label='id')
    #     except:
    #         data_frame_key_list = df.keys()
    #         field_list = ['name', 'family', 'email', 'phone', 'num_company_or_home', 'address']
    #         data_frame_key_list, fields_not_in_data_frame_keys_list = get_equal_items_list_one_in_list_tow(
    #             field_list, data_frame_key_list)
    #         add_file_form.add_error('file', f'این عنوان {fields_not_in_data_frame_keys_list} در  فایل وجود ندارد')
            # redirect('user_information:add_fil')
    return render(request, template_name='contact/add_contact_by_file_component.html', context=context)




