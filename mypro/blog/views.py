from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def base(request):
    return render(request,'base.html')
def index(request):
    # template 
    template = loader.get_template('index.html')

    # context data
    context = {
        # context data to be pulled from the DB
        'products' : Product.objects.all()
        # the above line of code is equivalent to SELECT * FROM product_table;
    }
    return HttpResponse(template.render(context, request))