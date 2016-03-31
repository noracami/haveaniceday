from django.shortcuts import render
from .models import TableOfMonth, Shift

# Create your views here.
def home(request):
    tables = TableOfMonth.objects.all()
    return render(request, 'tables_of_month/table_list.html', {'tables': tables})
    return render(request, 'website_component/home.html', {'ViewName': request})

#def table_list(request):
#    tables = TableOfMonth.objects.all()
#    return render(request, 'table_list.html', {'tables': tables})

def table_detail(request, pk):
    try:
        table = TableOfMonth.objects.get(pk=pk)
    except TableOfMonth.DoesNotExist:
        raise Http404
    return render(request, 'tables_of_month/table_detail.html', {'table': table})
