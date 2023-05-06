from django.forms import ModelForm
from .models import book


class BookForm(ModelForm):
    class Meta:
        model = book
        fields = ('book_name', 'author', 'isbn', 'co_author', 'release')
