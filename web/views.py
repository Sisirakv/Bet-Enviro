from django.shortcuts import render
from web.models import Category, Gallery, Product


from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .forms import contact_form
import json

# Create your views here.
def index(request):
    gallery = Gallery.objects.all()[:4]
    client = Client.objects.all()[:8]
    context = {
        "is_index" : True,
        "gallery" : gallery,
        "client" : client,
    }
    return render(request,"web/index.html",context)


def about_us(request):
    client = Client.objects.all()[:8]
    context = {
        "is_about_us" : True,
        "client" : client
    }
    return render(request,"web/about-us.html",context)


def services(request):
    service = Service.objects.all()
    context = {
        "is_services" : True,
        "service" : service,
    
    }
    return render(request,"web/services.html",context)



def product(request):
    category = Category.objects.filter(is_active = True)
    product = Product.objects.all()
    context = {
        "is_product" : True,
        "category" : category,
        "products" : product,
    }
    return render(request,"web/product.html",context)



def blog(request):
    blog = Blog.objects.all() 
    context = {
        "is_blog" : True,
        "blogs" : blog,
    }
    return render(request,"web/blog.html",context)

@csrf_exempt
def contact(request):
    forms = contact_form(request.POST or None)
    if request.method == "POST":
        print('hi')
        print(forms.errors) 
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
            
            
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context= {
            "is_contact" : True,
            "forms":forms,

        }
    return render(request,"web/contact.html",context)


def gallery(request):
    image = Gallery.objects.all()
    context = {
        "is_gallery" : True,
        "image": image,
    }
    return render(request,"web/gallery.html",context)


def client(request):
    client = Client.objects.all()
    context = {
        "client": client,
    }
    return render(request,"web/our clients.html",context)


def demo_services(request):
    main_service = Service.objects.all()
    sub_service = subService.objects.all()
    context = {
        "is_services" : True,
        "main_service": main_service,
        "sub_service" : sub_service,
    }
    return render(request,"web/demo service.html",context)


    

def water_QT_diag(request):
    return render(request,"web/water quality/wqt&diaganosis.html")

def water_QT(request):
    return render(request,"web/water quality/water-quality-test.html")

def waste_water(request):
    return render(request,"web/water quality/waste-water-treatment.html")




def Water_treat(request):
    return render(request,"web/water treatment/water-treatment.html")

def water_filter(request):
    return render(request,"web/water treatment/water filter/water-filter.html")

def sand_filter(request):
    return render(request,"web/water treatment/water filter/sand-filter.html")

def carbon_filter(request):
    return render(request,"web/water treatment/water filter/carbon-filter.html")

def iron_filter(request):
    return render(request,"web/water treatment/water filter/iron-filter.html")

def softner(request):
    return render(request,"web/water treatment/water filter/softener-hardner.html")

def dmf(request):
    return render(request,"web/water treatment/water filter/DMF.html")

def tmf(request):
    return render(request,"web/water treatment/water filter/TMF.html")



def water_purifier(request):
    return render(request,"web/water treatment/water purifier/water-purifier.html")

def ro(request):
    return render(request,"web/water treatment/water purifier/RO.html")

def uf(request):
    return render(request,"web/water treatment/water purifier/UF.html")

def uv(request):
    return render(request,"web/water treatment/water purifier/UV.html")

def cartbridge(request):
    return render(request,"web/water treatment/water purifier/cartbridge.html")

def alkaline(request):
    return render(request,"web/water treatment/water purifier/alkaline.html")




def germ_removal(request):
    return render(request,"web/water treatment/germ removal/germ-removal.html")

def ozonator(request):
    return render(request,"web/water treatment/germ removal/ozonators.html")

def uv_filter(request):
    return render(request,"web/water treatment/germ removal/uv-filters.html")

def chlorine_diffuser(request):
    return render(request,"web/water treatment/germ removal/chlorine-diffuser.html")

def chlorine_dozer(request):
    return render(request,"web/water treatment/germ removal/chlorine-dozer.html")



def water_dispenser(request):
    return render(request,"web/water treatment/water dispenser/water-dispenser.html")

def steel_water_dispenser(request):
    return render(request,"web/water treatment/water dispenser/steel-water-dispenser.html")

def fiber_water_dispenser(request):
    return render(request,"web/water treatment/water dispenser/fiber-water.html")

def pipeline(request):
    return render(request,"web/water treatment/pipeline-dirt.html")

def water_atm(request):
    return render(request,"web/water treatment/water-atms.html")





def commercial_ind(request):
    return render(request,"web/commercial and ind/commercial & ind.html")

def reverse_OS(request):
    return render(request,'web/commercial and ind/reverse os.html')

def ultra_filtration(request):
    return render(request,'web/commercial and ind/Ultra filtration.html')

def water_demineralize(request):
    return render(request,'web/commercial and ind/water demineralize.html')

def ozonation(request):
    return render(request,'web/commercial and ind/Ozonation.html')

def packaged_drinking(request):
    return render(request,'web/commercial and ind/packaged Drinking.html')

def carbonated_softdrink(request):
    return render(request,'web/commercial and ind/carbonated SD.html')

def pet_bottle(request):
    return render(request,'web/commercial and ind/pet bottle BM.html')


def waste_WT(request):
    return render(request,'web/waste water/waste WT.html')

def stp(request):
    return render(request,'web/waste water/STP.html')

def mbbr(request):
    return render(request,'web/waste water/MBBR.html')

def sbr(request):
    return render(request,'web/waste water/SBR.html')

def saff(request):
    return render(request,'web/waste water/SAFF.html')

def bio_digester(request):
    return render(request,'web/waste water/BIO DIGESTER.html')

def etp(request):
    return render(request,'web/waste water/ETP.html')

def grid_remover(request):
    return render(request,'web/waste water/grid remover.html')

def oil_trap(request):
    return render(request,'web/waste water/oil trap.html')

def food_WM(request):
    return render(request,'web/food waste/food WM.html')

def biogas(request):
    return render(request,'web/food waste/biogas.html')

def portable_bio(request):
    return render(request,'web/food waste/portable bio.html')

def underground_bio(request):
    return render(request,'web/food waste/underground bio.html')

def biocompost(request):
    return render(request,'web/food waste/biocompost.html')

def marker_waste(request):
    return render(request,'web/food waste/market waste.html')

def solid_WM(request):
    return render(request,'web/solid waste/solid WM.html')

def incinerator(request):
    return render(request,'web/solid waste/INCINERATOR.html')

def brick_made(request):
    return render(request,'web/solid waste/brick made.html')

def ss(request):
    return render(request,'web/solid waste/SS.html')

def ms(request):
    return render(request,'web/solid waste/MS.html')

def napkin(request):
    return render(request,'web/solid waste/napkin.html')

def napkin_vending(request):
    return render(request,'web/solid waste/napkin vending.html')

def plastic(request):
    return render(request,'web/solid waste/plastic.html')

def solar_energy(request):
    return render(request,'web/solar energy/solar energy.html')

def on_grid(request):
    return render(request,'web/solar energy/on grid.html')

def off_grid(request):
    return render(request,'web/solar energy/off grid.html')

def water_heater(request):
    return render(request,'web/solar energy/water heater.html')

def street_light(request):
    return render(request,'web/solar energy/street light.html')

def after_sale(request):
    return render(request,'web/after sale/after sale.html')

def amc(request):
    return render(request,'web/after sale/amc.html')

def chemical_treatment(request):
    return render(request,'web/after sale/WT chemical.html')

def wt_accessories(request):
    return render(request,'web/after sale/WT ass.html')

def resetting(request):
    return render(request,'web/after sale/resetting.html')

def swimming_pool(request):
    return render(request,'web/swimming pools/swimming-pools.html')

def skimmer_type(request):
    return render(request,'web/swimming pools/skimmer-type.html')

def overflow_type(request):
    return render(request,'web/swimming pools/overflow-type.html')

def infinity_type(request):
    return render(request,'web/swimming pools/infinity-type.html')

def rain_water_harvesting(request):
    return render(request,'web/rain water harvesting/rain-water-harvesting.html')

def wr_9_stage(request):
    return render(request,'web/rain water harvesting/wr-9stage.html')

def wr_8_stage(request):
    return render(request,'web/rain water harvesting/wr-8stage.html')

def wr_4_stage(request):
    return render(request,'web/rain water harvesting/wr-4stage.html')



def locate(request):
    return render(request,'web/locate ur service.html')


