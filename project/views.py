import datetime
import json
from collections import OrderedDict

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import *
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpResponseNotFound  
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q, Avg, Count
from django.template.defaultfilters import slugify

from car_price import settings
from functools import wraps
from project.models import *
from django.contrib.redirects.models import *

import re

def main(request):
    country_label = settings.COUNTRY
    currency_label = settings.CURRENCY

    if len(request.GET) > 0:
        return HttpResponsePermanentRedirect(request.path)
 
    try:
        currency = currency_label[request.POST["currency"]]
    except:
        currency = currency_label["USD"]

    res = OrderedDict()
    names = Car.objects.values('name').distinct().annotate(davg=Avg('price')).order_by("name")    

    for name in names:
        if name["davg"] == 0:
            continue

        car_per_country = Car.objects.filter(name=name["name"]).exclude(price=0) \
                                     .values('country') \
                                     .annotate(davg=Avg('price'))

        car_per_brand = Car.objects.filter(name=name["name"]).exclude(price=0) \
                                     .values('brand').distinct().order_by("brand")                                   
        
        '''prev_car_per_country = Car.objects.filter(name=name["name"]).exclude(prev_price=0) \
                                     .values('country') \
                                     .annotate(pavg=Avg('prev_price'))
        
        prev_car_per_country = {item["country"]:item for item in prev_car_per_country}'''

        temp_data = OrderedDict()
        temp_data["USA"], temp_data["UK"], temp_data["France"], temp_data["Germany"], temp_data["Italy"], temp_data["Switzerland"], = None, None, None, None,None, None        
         
        for item in car_per_country:
            if item["country"] in temp_data.keys():
                item["davg"] *= currency["currency_rate"]

                prev_price = 0
                percent = 0
                '''if item["country"] in prev_car_per_country:
                    prev_price = prev_car_per_country[item["country"]]["pavg"] * currency["currency_rate"]
                    percent = (item["davg"] - prev_price) * 100 / item["davg"]'''

                temp_data[item["country"]] = {"davg": int(item["davg"]), 
                                              "pavg": prev_price, 
                                              "percent": percent}

        res[name["name"]] = temp_data
        res[name["name"]]["brand"] = car_per_brand

    chartData = getChartData(dict(), currency["currency_rate"], type)
    menu = getMenu()
    car_name = None
    meta_description = "Visit Supercar Report to view Supercar Prices from around the world. The Supercar Prices are updated daily to provide you the most accurate Supercar Price Guide available. "

    return render_to_response('cars.html', locals(), context_instance=RequestContext(request))


def req_brand(request, car_name):

    redirects = Redirect.objects.all()
    for redirect_obj in redirects:
        if redirect_obj.old_path == request.path:
            return HttpResponsePermanentRedirect(redirect_obj.new_path)
    
    if len(request.GET) > 0:
        return HttpResponsePermanentRedirect(request.path)

    if len(car_name) < 7 or car_name[-7:] != "-prices":
        return HttpResponsePermanentRedirect(request.path[:-1] + "-prices/")

    currency_label = settings.CURRENCY

    try:
        currency = currency_label[request.POST["currency"]]
    except:
        currency = currency_label["USD"]

    temp_name = car_name[:-7]
    carnames = Make.objects.all()
    for item in carnames:
        alias = slugify(item.alias)
        if temp_name == alias:
            break
        elif bool(re.search('^' + alias, temp_name)):
            car_name = alias
            brand_name = re.sub("^" + alias, "", temp_name)[1:]
            print temp_name, alias, brand_name
            res = req_year(currency, car_name, brand_name)

            make = Make.objects.filter(name=getNameFromSlug(car_name, "name")).first()
            model = make.model_set.filter(name=getNameFromSlug(brand_name, "brand")).first()
            price = model.price_set.all()
            if res["type"] == "redirect":
                return HttpResponsePermanentRedirect(res["value"])
            elif res["type"] == "404":
                return HttpResponseNotFound('<h1>No Page Here (404)</h1>')
            else:
                # templist = res["value"]
                # templist.extend({"list": ["A","C","E"]})
                # res["value"] = templist
                res["value"]["prices"] = price
                res["value"]["currency"] = currency
                return render_to_response('cars.html', res["value"], context_instance=RequestContext(request))
                #return render_to_response('cars.html', locals(), context_instance=RequestContext(request))

    car_name = car_name[:-7]

    country_label = settings.COUNTRY
    tp_car_name = car_name
    car_name = getNameFromSlug(car_name, "name")

    '''if not car_name:
        redirects = Redirect.objects.all()
        for redirect_obj in redirects:
            if redirect_obj.old_path in ["/%s/" % tp_car_name, "/%s" % tp_car_name]:
                return HttpResponsePermanentRedirect(redirect_obj.new_path)        

        return HttpResponseNotFound('<h1>No Page Here (404)</h1>')'''

    res = OrderedDict()

    brands = Car.objects.filter(name=car_name).values('brand').distinct().annotate(davg=Avg('price')).order_by("brand")


    for brand in brands:
        if brand["davg"] == 0:
            continue

        car_per_country = Car.objects.filter(name=car_name, brand=brand["brand"]).exclude(price=0) \
                                     .values('country') \
                                     .annotate(davg=Avg('price'))
        '''prev_car_per_country = Car.objects.filter(name=car_name, brand=brand["brand"]).exclude(prev_price=0) \
                                     .values('country') \
                                     .annotate(pavg=Avg('prev_price'))

        prev_car_per_country = {item["country"]:item for item in prev_car_per_country}'''

        make = Make.objects.filter(name=car_name).first()
        model = make.model_set.filter(name=brand["brand"]).first()
        
        price = model.price_set.annotate(usa_l_price=Avg('usa_low_price'),
            usa_a_price=Avg('usa_avg_price'),
            usa_h_price=Avg('usa_high_price'),
            uk_l_price=Avg('uk_low_price'),
            uk_a_price=Avg('uk_avg_price'),
            uk_h_price=Avg('uk_high_price'))

        temp_data = OrderedDict()
        temp_data["USA"], temp_data["UK"], temp_data["France"], temp_data["Germany"], temp_data["Italy"], temp_data["Switzerland"], = None, None, None, None,None, None        
         
        # for item in car_per_country:
        #     if item["country"] in temp_data.keys():
        #         item["davg"] *= currency["currency_rate"]

        #         prev_price = 0
        #         percent = 0
        #         '''if item["country"] in prev_car_per_country:
        #             prev_price = prev_car_per_country[item["country"]]["pavg"] * currency["currency_rate"]
        #             percent = (item["davg"] - prev_price) * 100 / item["davg"]'''

        #         temp_data[item["country"]] = {"davg": int(item["davg"]), 
        #                                       "pavg": prev_price, 
        #                                       "percent": percent}

        # print price
        if price.count() > 1:
            print price[0]
            res[brand["brand"]] = [price[0]]

    chartData = getChartData({"car_name": car_name}, currency["currency_rate"])
    menu = getMenu()
    meta_description = "Visit Supercar Report to view {} Prices from around the world. The {} Prices are updated weekly to provide you the most accurate {} Price Guide available.".format(car_name,car_name,car_name)
    return render_to_response('cars.html', locals(), context_instance=RequestContext(request))


def req_year(currency, car_name, brand):
    '''if len(request.GET) > 0:
        return HttpResponsePermanentRedirect(request.path)

    flag = 0
    path = request.path.split("/")

    if len(car_name) < 7 or car_name[-7:] != "-prices":
        flag = 1
        path[-3] = car_name+"-prices"
    if len(brand) < 7 or brand[-7:] != "-prices":
        flag = 1
        path[-2] = brand+"-prices"

    if flag == 1:
        return HttpResponsePermanentRedirect("/".join(path))

    car_name = car_name[:-7]
    brand = brand[:-7]'''

    country_label = settings.COUNTRY
    currency_label = settings.CURRENCY

    car_name = getNameFromSlug(car_name, "name")
    car_brand = getNameFromSlug(brand, "brand")
    tp_car_name = car_name
    tp_car_brand = car_brand

    if not car_name and not car_brand:
        redirects = Redirect.objects.all()
        for redirect_obj in redirects:
            if redirect_obj.old_path == response.path:
                return {"type": "redirect", "value": redirect_obj.new_path}
    
    if not car_name or not car_brand:
        return {"type": "404"}
        
    brand = car_brand

    res = OrderedDict()
    years = Car.objects.filter(name=car_name, brand=brand).exclude(price=0).values('year').distinct().order_by("-year")


    for year in years:
        car_per_country = Car.objects.filter(name=car_name, brand=brand, year=year["year"]).exclude(price=0) \
                                     .values('country') \
                                     .annotate(davg=Avg('price'))
        '''prev_car_per_country = Car.objects.filter(name=car_name, brand=brand, year=year["year"]).exclude(prev_price=0) \
                                     .values('country') \
                                     .annotate(pavg=Avg('prev_price'))

        prev_car_per_country = {item["country"]:item for item in prev_car_per_country}'''

        temp_data = OrderedDict()
        temp_data["USA"], temp_data["UK"], temp_data["France"], temp_data["Germany"], temp_data["Italy"], temp_data["Switzerland"], = None, None, None, None,None, None        
         
        for item in car_per_country:
            if item["country"] in temp_data.keys():
                item["davg"] *= currency["currency_rate"]

                prev_price = 0
                percent = 0
                '''if item["country"] in prev_car_per_country:
                    prev_price = prev_car_per_country[item["country"]]["pavg"] * currency["currency_rate"]
                    percent = (item["davg"] - prev_price) * 100 / item["davg"]'''

                temp_data[item["country"]] = {"davg": int(item["davg"]), 
                                              "pavg": prev_price, 
                                              "percent": percent}

        res[year["year"]] = temp_data

    chartData = getChartData({"car_name": car_name, "car_brand": car_brand}, currency["currency_rate"])
    menu = getMenu()
    meta_description = "Visit Supercar Report to view {} {} Prices from around the world. The {} {} Prices are updated weekly to provide you the most accurate {} {} Price Guide available.".format(car_name, car_brand, car_name, car_brand, car_name, car_brand)

    rt_value = {"car_name": car_name, "car_brand": car_brand, "res": res, "country_label": country_label, "currency_label": currency_label, "chartData":chartData,
                  "menu": menu, "meta_description": meta_description}

    return {"type": "page", "value": rt_value}

def redirect_url(request, car_name, brand):
    return HttpResponsePermanentRedirect("/%s-%s" % (car_name, brand))


def getMenu():
    names = Car.objects.values('name').annotate(count=Avg('price')).order_by("name")

    res = OrderedDict()
    for name in names:
        if name["count"] == 0:
            continue
   
        temp = Car.objects.filter(name=name["name"]).values('brand').annotate(count=Count('brand'), avg=Avg('price')).order_by("brand")
        
        new = []
        for item in temp:
            if item["avg"] != 0:
                new.append(item)

        res[name["name"]] = [name, new]
 
    return res

def getChartData(param, currency_rate, type=None):
    # get chart data
    years = Car.objects.values('year').distinct()

    years = [item["year"] for item in years]
    years = sorted(years, key=int, reverse=False)
    years = [int(item) for item in years]

    chartData = []    

    if type != None:
        tp_chartData = OrderedDict()

        temp = Car.objects.all().values("year", "name").annotate(davg=Avg('price')).order_by("name")
        for item in temp:
            if item["davg"] == 0:
                continue

            if item["name"] not in tp_chartData:
                tp_chartData[item["name"]] = []

            tp_chartData[item["name"]].append([float(item["year"]), item["davg"]])

    
        for name in tp_chartData:
            data = sorted(tp_chartData[name], key=getKey)
            chartData.append({"name": name, "data": data})


    if "car_brand" in param:
        temp = Car.objects.filter(name=param['car_name'], brand=param['car_brand']).exclude(price=0) \
                          .values("year", "country") \
                          .annotate(davg=Avg('price')) \
                          .order_by("country")
    elif "car_name" in param:
        temp = Car.objects.filter(name=param['car_name']).exclude(price=0).values("year", "country") \
                           .annotate(davg=Avg('price')).order_by("country")
    else:
        temp = Car.objects.all().exclude(price=0).values("year", "country") \
                           .annotate(davg=Avg('price')).order_by("country")

    tp_chartDataForCountry = OrderedDict()
    for item in temp:
        if item["country"] not in tp_chartDataForCountry:
            tp_chartDataForCountry[item["country"]] = []

        tp_chartDataForCountry[item["country"]].append([float(item["year"]), item["davg"]])

    chartDataForCountry = []
    # for name in tp_chartDataForCountry:   ##@@##
    for country in settings.COUNTRY:
        name = country['name']
        if name not in tp_chartDataForCountry:
            continue

        data = sorted(tp_chartDataForCountry[name], key=getKey)
        chartDataForCountry.append({"name": name, "data": data})

    return [chartData, chartDataForCountry, years]


def getNameFromSlug(slug, type):
    if type == "name":
        names = Car.objects.values('name').distinct()
        names = {slugify(name["name"]):name["name"] for name in names}

        return names.get(slug)
    elif type == "brand":
        brands = Car.objects.values('brand').distinct()
        brands = {slugify(brand["brand"]):brand["brand"] for brand in brands}

        return brands.get(slug)


def getKey(item):
    return item[0]
