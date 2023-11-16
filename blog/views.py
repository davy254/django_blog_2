from django.shortcuts import render

# Create your views here.
def hompage(request):

    return render(request, "blog/index.html")