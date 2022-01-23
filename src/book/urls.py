from django.urls import path
from .views import (
        BookSortingView,
        boos_view
    )

app_name = 'books'

urlpatterns = [
    path('', BookSortingView.as_view(), name='main-board'),
    path('<pk>/', boos_view, name='book'),
]
