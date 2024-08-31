from django import forms
from .models import Book
from datetime import date
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'bookTitle',
            }
        )
    )
    author = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'bookAuthor',
            }
        )
    )
    year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'bookYear',
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'bookDescription',
                'rows': 3,
            }
        )
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'bookPrice',
            }
        )
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'id': 'bookImage',
            }
        )
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'description', 'price', 'image']

    def clean_year(self):
        year = self.cleaned_data.get('year')
        current_year = date.today().year
        if year > current_year:
            raise ValidationError("Kitob chiqarilgan yili joriy yildan keyin bo'lishi mumkin emas.")
        return year

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 1:
            raise ValidationError("Kitob narxi musbat qiymat bo'lishi kerak.")
        return price

    def update(self, book):
        book.title = self.cleaned_data.get('title')
        book.author = self.cleaned_data.get('author')
        book.year = self.cleaned_data.get('year')
        book.description = self.cleaned_data.get('description')
        book.price = self.cleaned_data.get('price')
        book.image = self.cleaned_data.get('image')
        book.save()
        return book
