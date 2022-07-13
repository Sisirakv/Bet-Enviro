from django.urls import path
from . import views


app_name='web'

urlpatterns = [
    path("",views.index,name='index'),
    path("product/",views.product,name='product'),
    path("contact/",views.contact,name='contact'),
    path("gallery/",views.gallery,name='gallery'),
    path("blog/",views.blog,name='blog'), 
    path("services/",views.services,name='services'), 
    path("About us/",views.about_us,name="About us"),


    path('Water QT & diag/', views.water_QT_diag,name='Water QT & diag'),
    path('Water QT/',views.water_QT,name="Water QT"),
    path('Waste Water QT/',views.waste_water,name='Waste Water QT'),


    path('Water Treatment/',views.Water_treat,name='Water Treatment'),

    path('Water Filter/',views.water_filter,name='Water Filter'),
    path('Sand Filter/',views.sand_filter,name='Sand Filter'),
    path('Carbon Filter/',views.carbon_filter,name='Carbon Filter'),
    path('Iron Filter/',views.iron_filter,name='Iron Filter'),
    path('Softner Hardner/',views.softner,name='Softner Hardner'),
    path('DMF/',views.dmf,name='DMF'),
    path('TMF/',views.tmf,name='TMF'),

    path('Water Purifier/',views.water_purifier,name='Water Purifier'),
    path('RO/',views.ro,name='RO'),
    path('UF/',views.uf,name='UF'),
    path('UV/',views.uv,name='UV'),
    path('Cartbridge/',views.cartbridge,name='Cartbridge'),
    path('Alkaline/',views.alkaline,name='Alkaline'),

    path('Germ Removal/',views.germ_removal,name='Germ Removal'),
    path('Ozonator/',views.ozonator,name='Ozonator'),
    path('UV Filter/',views.uv_filter,name='UV Filter'),
    path('Chlorine Diffuser/',views.chlorine_diffuser,name='Chlorine Diffuser'),
    path('Chlorine Dozer/',views.chlorine_dozer,name='Chlorine Dozer'),

    path('Water Dispenser',views.water_dispenser,name="Water Dispenser"),
    path('Steel Water Dispenser',views.steel_water_dispenser,name="Steel Water Dispenser"),
    path('Fiber Water Dispenser',views.fiber_water_dispenser,name="Fiber Water Dispenser"),

    path('Water ATMs',views.water_atm,name="Water ATMs"),

    path('Pipeline',views.pipeline,name="Pipeline"),






    path('Commercials and industrial WT/',views.commercial_ind,name="Commercials and industrial WT"),
    path('Rverse OS/',views.reverse_OS,name="Rverse OS"),
    path('Ultra Filtertion/',views.ultra_filtration,name="Ultra Filtertion"),
    path('Water Demineralize/',views.water_demineralize,name="Water Demineralize"),
    path('Ozonation/',views.ozonation,name="Ozonation"),
    path('Packaged Drinking/',views.packaged_drinking,name="Packaged Drinking"),
    path('Carbonated Soft Drink/',views.carbonated_softdrink,name="Carbonated Soft Drink"),
    path('Pet Bottle BM/',views.pet_bottle,name="Pet Bottle BM"),

    path('Waste Water Treatment/',views.waste_WT,name="Waste Water Treatment"),
    path('STP/',views.stp,name="STP"),
    path('MBBR/',views.mbbr,name="MBBR"),
    path('SBR/',views.sbr,name="SBR"),
    path('SAFF/',views.saff,name="SAFF"),
    path('BIO DIGESTER/',views.bio_digester,name="BIO DIGESTER"),
    path('ETP/',views.etp,name="ETP"),
    path('Grid Remover System/',views.grid_remover,name="Grid Remover System"),
    path('Oil Trap/',views.oil_trap,name="Oil Trap"),

    path('Food WM/',views.food_WM,name="Food WM"),
    path('Biogas/',views.biogas,name="Biogas"),
    path('Portable Biogas/',views.portable_bio,name="Portable Biogas"),
    path('Underground Biogas/',views.underground_bio,name="Underground Biogas"),
    path('Biocompost/',views.biocompost,name="Biocompost"),
    path('Market Waste/',views.marker_waste,name="Market Waste"),

    path('Solid WM/',views.solid_WM,name="Solid WM"),
    path('INCINERATOR/',views.incinerator,name="INCINERATOR"),
    path('Brick made/',views.brick_made,name="Brick made"),
    path('SS/',views.ss,name="SS"),
    path('MS/',views.ms,name="MS"),
    path('Napkin Incinerator/',views.napkin,name="Napkin Incinerator"),
    path('Napkin Vending/',views.napkin_vending,name="Napkin Vending"),
    path('Plastic Recycling/',views.plastic,name="Plastic Recycling"),
    
    path('Solar Energy/',views.solar_energy,name="Solar Energy"),
    path('On Grid/',views.on_grid,name="On Grid"),
    path('Off Grid/',views.off_grid,name="Off Grid"),
    path('Water Heater/',views.water_heater,name="Water Heater"),
    path('Street light/',views.street_light,name="Street light"),

    path('After Sale/',views.after_sale,name="After Sale"),
    path('AMC/',views.amc,name="AMC"),
    path('WT Chemical/',views.chemical_treatment,name="WT Chemical"),
    path('WT Accessories/',views.wt_accessories,name="WT Accessories"),
    path('Resetting/',views.resetting,name="Resetting"),






    path('Locate Service/',views.locate,name="Locate Service")

]