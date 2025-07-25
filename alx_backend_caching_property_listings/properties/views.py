from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    return render(request, 'properties/list.html', {'properties': properties})

