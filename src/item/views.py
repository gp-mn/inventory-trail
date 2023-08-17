from django.shortcuts import render
from .models import ItemGroup
from django.core import serializers
from django.http import HttpResponse
import json

# Create your views here.
def slug_view(request, slug):
    obj = ItemGroup.objects.get(slug=slug)
    context = {"item":obj}
    return render(request, "slug.html", context)
# Create your views here.
def item_group_detail_page(request):
    historicals = serializers.serialize("json", ItemGroup.objects.all())
    context = {'historicals' : historicals}
    template = 'checkout.html'
    return HttpResponse(template.render(context, request))

