from django.shortcuts import render
from .models import TableOfMonth, Shift

# Create your views here.
def home(request):
    return render(request, 'home.html')

def table_list(request):
    tables = TableOfMonth.objects.all()
    return render(request, 'table_list.html', {'tables': tables})

def table_detail(request, pk):
    try:
        table = TableOfMonth.objects.get(pk=pk)
    except TableOfMonth.DoesNotExist:
        raise Http404
    return render(request, 'table_detail.html', {'table': table})
