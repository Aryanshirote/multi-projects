from django.shortcuts import render

def dashboards(request):
    return render(request, "app5/dashboard.html")
