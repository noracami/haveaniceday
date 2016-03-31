from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website_component/home.html', {'ViewName': request})

def order_list(request):
    return render(request, 'order_list.html', {})

def order_detail(request, pk):
    #try:
    #    table = TableOfMonth.objects.get(pk=pk)
    #except TableOfMonth.DoesNotExist:
    #    raise Http404
    return render(request, 'order_detail.html', {})
