from django.http import JsonResponse
from django.shortcuts import render

from .models import (Category, Location, Product, Professional, Specialist,
                     UserBase)

# Create your views here.



def home(request):
    categories = Category.objects.all()
    professionals = Professional.objects.filter(specialization__name = "Shipakerler")[:3]
    users = UserBase.objects.all()
    category = request.GET.get("category")
    
    if category is not None:
        if category == "Shipakerler":
            professionals2 = Professional.objects.filter(specialization__name = "Shipakerler")[:3]
        else:
            professionals2 = Professional.objects.filter(specialization__name = "Yuristler")[:3]

        professionals3 = []
        for pro in professionals2:
            d = {}
            d['first_name'] = pro.first_name
            d['last_name'] = pro.last_name
            d['location'] = pro.locations.where
            d['image'] = pro.image.url
            d['specialists'] = []
            for s in pro.specialists.all():
                d['specialists'].append(s.name)
            professionals3.append(d)
            
        return JsonResponse({'professionals': professionals3})


    context = {
        "categories": categories,
        "professionals": professionals,
        "users": users,
    }
    return render(request, "page/home.html", context)


def view_more(request):
    what = request.GET.get("what")
    professionals = Professional.objects.filter(specialization__name = what)
    locations = Location.objects.all()
    categories = Specialist.objects.filter(specialization = what.replace("ler", "").upper())
    context = {
        "what": what,
        "professionals": professionals,
        "locations": locations,
        "categories": categories
    }
    return render(request, "page/view_more.html", context)

def apte_kar(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "page/aptekar.html", context)


"""
        <!-- OUR JETISKENLIK -->
        <div class="container row justify-content-lg-between justify-content-md-center home__jetiskenlik">
            <div class="col-4 offset-lg-1 col-md-4 col-lg-2 jetiskenlik__info">
                <span class="home_jetiskenlik_icon"><i class="fa-regular fa-star star__icon"></i></span>
                <div class="jetiskenlik__about">
                    <h4>15+ jil </h4>
                    <span>Tájiriybe</span>
                </div>
            </div>
            <div class="col-4 col-md-4 col-lg-2 jetiskenlik__info">
                <span class="home_jetiskenlik_icon"><i class="fa-solid fa-stethoscope stethoscope__icon"></i></span>
                <div class="jetiskenlik__about">
                    <h4>50+</h4>
                    <span>Medicinalıq qánigelikler</span>
                </div>
            </div>
            <div class="col-4 col-md-4 col-lg-2 jetiskenlik__info">
                <span class="home_jetiskenlik_icon"><i class="fa-solid fa-gavel lawyer__icon"></i></span>
                <div class="jetiskenlik__about">
                    <h4>34+</h4>
                    <span>Yurist qánigelikler</span>
                </div>
            </div>
            <div class="col-4 col-md-6 col-lg-2 jetiskenlik__info">
                <span class="home_jetiskenlik_icon"><i class="fa-regular fa-face-smile face__icon"></i></span>
                <div class="jetiskenlik__about">
                    <h4>10.000+</h4>
                    <span>Qanaatlanǵan klientler</span>
                </div>
            </div>
            <div class="col-4 col-md-6 col-lg-2 jetiskenlik__info">
                <span class="home_jetiskenlik_icon"><i class="fa-solid fa-video video__icon"></i></span>
                <div class="jetiskenlik__about">
                    <h4>40.000 min</h4>
                    <span>onlayn-máslahátlar</span>
                </div>
            </div>
        </div>
        <!-- END OUR JETISKENLIK -->

"""