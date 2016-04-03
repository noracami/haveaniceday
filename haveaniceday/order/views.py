from django.shortcuts import get_object_or_404, render
from .models import Member

# Create your views here.
def home(request):
    return render(request, 'order/order_list.html', {})
    return render(request, 'website_component/home.html', {'ViewName': request})

def member_list(request):
    """
    docstring for member_list
    """
    members = Member.objects.all()
    return render(request, 'order/member_list.html', {'members': members})


def member_detail(request):
    m = 'empty'
    if 'id' in request.GET:
        m = get_object_or_404(Member, pk=request.GET['id'])
    return render(request, 'order/member_detail.html', {'member': m})

def order_list(request):
    return render(request, 'order/order_list.html', {})

def order_detail(request, pk):
    #try:
    #    order = Order.objects.get(pk=pk)
    #except Order.DoesNotExist:
    #    raise Http404
    return render(request, 'order_detail.html', {})
