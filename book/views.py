from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import BookForm
from .models import Book


class DashboardView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            'title': "Bosh sahifa",
            'books': books,
        }
        return render(request, 'dashboard.html', context)


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            'title': "Kitoblar",
            'books': books,
        }
        return render(request, 'books.html', context)


class AddBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Kitob muvaffaqiyatli qo'shildi!")
            return redirect('books')
        else:
            messages.error(request, "Iltimos, barcha maydonlarni to'g'ri to'ldiring!")
        return render(request, 'add_book.html', {'form': form})


class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, 'book_detail.html', {'book': book, 'form': form})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Kitob muvaffaqiyatli yangilandi!")
            return redirect('book_detail', pk=book.pk)
        messages.error(request, "Iltimos, barcha maydonlarni to'g'ri to'ldiring!")
        return render(request, 'book_detail.html', {'book': book, 'form': form})


class BookDeleteView(View):
    def post(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            messages.warning(request, "Kitob muvaffaqiyatli o'chirildi!")
        except:
            messages.error(request, "Qandaydur xatolik yuz berdi!")
            return redirect('books')
        return redirect('books')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {'title': 'About Us'})


class ContactView(View):
    def get(self, request):
        # GET so'roviga forma ko'rsatish
        return render(request, 'contact.html', {
            'title': 'Biz bilan bog\'laning'
        })

    def post(self, request):
        messages.success(request, "Xabar qabul qilindi.")
        return redirect('contact')
