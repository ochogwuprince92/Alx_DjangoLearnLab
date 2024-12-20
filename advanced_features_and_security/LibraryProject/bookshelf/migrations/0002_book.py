# Generated by Django 4.2.11 on 2024-11-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
            options={
                'permissions': [('can_view', 'Can view book'), ('can_create', 'Can create book'), ('can_edit', 'Can edit book'), ('can_delete', 'Can delete book')],
            },
        ),
    ]
