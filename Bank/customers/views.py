from django.shortcuts import render
from customers import models
from haystack.query import SearchQuerySet 
from django.db.models import Count, Q
# Create your views here.

def index(request):
    template_name = "index.html" 
    if request.method == 'GET':
        keyword = request.GET.get('search')
        if keyword:
            results = SearchQuerySet().filter(Q(first_name__contains=keyword) | Q(last_name__contains=keyword)).load_all().models(models.Customer)  
        else:
            results = "" 
        context = {
            'results': results,
        }
        return render(request, template_name, context)