
from django.urls import path



from .views import AddBookView, GetBooksView

urlpatterns = [
    path('', GetBooksView.as_view()),
    path('create/', AddBookView.as_view()),
]