from django.shortcuts import render

def Index(request):
    context = {}
    return render(request, 'home/index.html', context)
