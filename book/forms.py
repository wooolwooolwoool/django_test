from django import forms
from .models import *

class BookshelfForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookshelfForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Bookshelf
        fields = ('title','cat')
        widgets = {
                    'title': forms.TextInput(attrs={'placeholder':'タイトル（50字まで）',}),
                    'category': forms.Select(),
                     }

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields['title'].widget.attrs['readonly'] = 'readonly'
        self.fields['isbn'].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Book
        fields = ('title', 'isbn','comment')
        widgets = {
                    'title': forms.TextInput(),
                    'isbn': forms.TextInput(),
                    'comment': forms.Textarea(attrs={'placeholder':'コメント（100字まで）','cols': 1, 'rows': 5}),
                }

BookFormset = forms.inlineformset_factory(
    Bookshelf, Book, BookForm, fields='__all__',
    extra=0, max_num=10,
)