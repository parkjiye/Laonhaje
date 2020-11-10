from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})
def about(request):
    return render(request, 'about.html', {})
def contact(request):
    return render(request, 'contact.html', {})
def blog(request):
    return render(request, 'blog.html', {})
def single(request):
    return render(request, 'single.html', {})
def typography(request):
    return render(request, 'typography.html', {})
def coupon(request):
    return render(request, 'coupon.html', {})
# Create your views here.
