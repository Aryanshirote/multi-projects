from django.shortcuts import render

def resume(request):
    return render(request, "app2/resume.html")
