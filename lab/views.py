from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'lab/index.html', {'message': 'Hello World'})
