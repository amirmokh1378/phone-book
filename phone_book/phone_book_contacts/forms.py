from django import forms
from phone_book_contacts.models import Contact, ContactFile


class AddForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['anonymous_account']

    def save(self, anonymous_account, commit=True):

        obj = super(AddForm, self).save(commit=False)
        obj.anonymous_account = anonymous_account
        obj.save()


class AddFileForm(forms.ModelForm):
    class Meta:
        model = ContactFile
        fields = '__all__'


