from django.shortcuts import render

# Create your views here.
def base(request):

    return render(request,"web/index.html")

def product(request):

    return render(request,"web/product.html")

def contact(request):

    return render(request,"web/contact.html")

def gallery(request):

    return render(request,"web/gallery.html")

def blog(request):

    return render(request,"web/blog.html")

def services(request):

    return render(request,"web/services.html")


def about_us(request):
    return render(request,"web/about-us.html")