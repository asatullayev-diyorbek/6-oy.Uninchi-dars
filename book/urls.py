from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('book/list/', views.BookListView.as_view(), name='books'),
    path('book/add-book/', views.AddBookView.as_view(), name='add_book'),
    path('book/<int:pk>/detail/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book'),

    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]