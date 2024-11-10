from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Customize list view: fields to be displayed in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search capability for title and author
    search_fields = ('title', 'author')
    
    # Add filter options for publication year
    list_filter = ('publication_year',)

# Register the Book model with the customized BookAdmin
admin.site.register(Book, BookAdmin)