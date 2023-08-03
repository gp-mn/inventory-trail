from django.shortcuts import render

from .models import ItemGroup

# Create your views here.
def slug_view(request, slug):
    obj = ItemGroup.objects.get(slug=slug)
    context = {"item":obj}
    return render(request, "slug.html", context)