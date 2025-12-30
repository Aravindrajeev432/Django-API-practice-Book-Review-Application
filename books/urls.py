
from django.urls import path


from .views import GetBooksView

urlpatterns = [
    path('', GetBooksView.as_view()),
]