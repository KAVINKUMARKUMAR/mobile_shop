from django.shortcuts import render

def create_error(request,exception):
    return render(request,'404.html', status=404)