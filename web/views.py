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

def water_QT_diag(request):
    return render(request,"web/wqt&diaganosis.html")

def water_QT(request):
    return render(request,"web/water-quality-test.html")

def waste_water(request):
    return render(request,"web/waste-water-treatment.html")


def Water_treat(request):
    return render(request,"web/water-treatment.html")

def water_filter(request):
    return render(request,"web/water-filter.html")

def sand_filter(request):
    return render(request,"web/sand-filter.html")

def carbon_filter(request):
    return render(request,"web/carbon-filter.html")

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