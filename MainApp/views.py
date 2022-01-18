from django.shortcuts import render, get_object_or_404
from .models import Tovar


# Create your views here.
def index(request):
    tovars_list = Tovar.objects.filter(available=True).order_by('-created')[:8]
    return render(request, "MainApp/index.html", {
        'tovars_list': tovars_list,
    })


def deteilProduct(request, slug):
    tovar = get_object_or_404(Tovar,
                              slug=slug,
                              available=True)
    return render(request, "MainApp/single-product.html", {
        'tovar': tovar,
    })
