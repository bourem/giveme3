from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

def index(request):
    items = Item.objects.all()
    return HttpResponse("index - " + ",".join([str(i.pk) for i in items]))

def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, 'giveme3/item_detail.html', context)
