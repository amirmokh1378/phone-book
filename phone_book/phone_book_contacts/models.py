from django.core.exceptions import ValidationError
from django.db import models
from phone_book_accounts.models import AnonymousAccount
import os
from django.db.models import Q


# Create your models here.


def contact_image_directory_path(instance, filename):
    base_name, ext = os.path.splitext(filename)
    return f'UserInFo/{instance}/{instance}{ext}'


class ContactManager(models.Manager):
    def search(self, anonymous_account, name='', family='', email='', phone='', num_company_or_home='', address='',
               ):
        lookup = Q(name__icontains=name) & Q(family__icontains=family) & Q(email__icontains=email) & Q(
            phone__icontains=phone) & Q(num_company_or_home__icontains=num_company_or_home) & Q(
            address__icontains=address)
        return anonymous_account.contact_set.filter(lookup).distinct()


class Contact(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=10, blank=True, default='')
    num_company_or_home = models.CharField(max_length=20, blank=True, default='')
    address = models.TextField(max_length=400, blank=True, default='')
    image = models.ImageField(upload_to=contact_image_directory_path, blank=True, default='')
    anonymous_account = models.ForeignKey(AnonymousAccount, on_delete=models.CASCADE)

    objects = ContactManager()

    def __str__(self):
        return self.name


def set_name_and_folder_excel_file(instance, filename):
    baseName, extension = os.path.splitext(filename)
    return f'excel_file/{baseName}{extension}'


class ContactFile(models.Model):
    file = models.FileField(upload_to=set_name_and_folder_excel_file)

    def check_extension(self):
        name, extension = os.path.splitext(self.file.name)
        if extension == '.xlsx':
            return 'xlsx'
        if extension == '.csv':
            return 'csv'
        raise ValidationError('the file must be excel or csv')
