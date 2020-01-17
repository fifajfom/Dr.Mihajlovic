from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,'website/index.html')

def Contact(request):
    return render(request,'website/contact.html')

def Gallery(request):
    return render(request,'website/gallery.html')
    
def Onama(request):
    return render(request,'website/index.html#onama')
