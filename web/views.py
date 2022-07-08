from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "is_index" : True,
    }
    return render(request,"web/index.html",context)


def about_us(request):
    context = {
        "is_about_us" : True,
    }
    return render(request,"web/about-us.html",context)


def services(request):
    context = {
        "is_services" : True,
    }
    return render(request,"web/services.html",context)



def product(request):
    context = {
        "is_product" : True,
    }
    return render(request,"web/product.html",context)



def blog(request):
    context = {
        "is_blog" : True,
    }
    return render(request,"web/blog.html",context)



def contact(request):
    context = {
        "is_contact" : True,
    }
    return render(request,"web/contact.html",context)



def gallery(request):
    context = {
        "is_gallery" : True,
    }
    return render(request,"web/gallery.html",context)









