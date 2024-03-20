from django.shortcuts import render
from django.views import generic
from .forms import *
from .models import *

# Create your views here.
class ScheduleList(generic.ListView):
    queryset = Schedule.objects.all()
    template_name = "book/schedule_list.html"
    book_form = BookForm()


def book_detail(request):
        book_form = BookForm()
        if request.method == 'POST':
            book_form = BookForm(request.POST)
            if book_form.is_valid():
                print(book_form.cleaned_data)
                # book = book_form.save()
                # book.author = request.user
                # book.save()
        else:
            book_form = BookForm()
        return render(
            request,
           'book/schedule_list.html',
            {
            'form': book_form,
            },
)

