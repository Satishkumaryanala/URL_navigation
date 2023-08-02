from django.shortcuts import render

# Create your views here.

def netflix(request):
    return render(request,'netflix.html')