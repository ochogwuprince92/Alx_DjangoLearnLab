# Generated by Django 4.2.11 on 2024-11-10 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add a book'), ('can_change_book', 'Can change a book'), ('can_delete_book', 'Can delete a book')]},
        ),
    ]
