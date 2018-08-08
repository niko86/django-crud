from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'lab/index.html', {'message': 'Hello World'})

class AnotherView(View):

    def get(self, request):
        return render(request, 'lab/another.html')
