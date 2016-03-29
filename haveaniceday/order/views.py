from django.shortcuts import render

# Create your views here.



def order_list(request):
    return render(request, 'order_list.html', {})

def order_detail(request, pk):
    #try:
    #    table = TableOfMonth.objects.get(pk=pk)
    #except TableOfMonth.DoesNotExist:
    #    raise Http404
    return render(request, 'order_detail.html', {})
