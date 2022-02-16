# Generated by Django 4.0.2 on 2022-02-16 10:55

from django.db import migrations, models
import django.db.models.deletion
import phone_book_contacts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('phone_book_accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=phone_book_contacts.models.set_name_and_folder_excel_file)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('family', models.CharField(blank=True, default='', max_length=20)),
                ('email', models.EmailField(blank=True, default='', max_length=100)),
                ('phone', models.CharField(blank=True, default='', max_length=10)),
                ('num_company_or_home', models.CharField(blank=True, default='', max_length=20)),
                ('address', models.TextField(blank=True, default='', max_length=400)),
                ('image', models.ImageField(blank=True, default='', upload_to=phone_book_contacts.models.contact_image_directory_path)),
                ('anonymous_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone_book_accounts.anonymousaccount')),
            ],
        ),
    ]
