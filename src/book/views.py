from django.shortcuts import render
from .models import Book

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView

class BookSortingView(ListView):
    queryset = Book.objects.all()
    template_name = 'books/main.html'


@csrf_exempt
def sort(self):
    books = json.loads(self.request.POST.get('sort'))
    for b in books:
        book = get_object_or_404(Book, pk=int(b['pk']))
        book.position = b['order']
        book.save()
    return HttpResponse('saved')

def boos_view(request,pk):
    obj = Book.objects.get(pk=pk)
    context = {
        'obj': obj,
    }
    return render(request, 'books/index.html', context)
