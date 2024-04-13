from django.shortcuts import render
from .models import Product

# Create your views here.
def homepage(request):
     if request.method == 'GET':
      data = Product.objects.all().values()
      return render(request, "homepage.html", {
         "products": data
      })