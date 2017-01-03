#!/usr/bin/python
import os
from os import sys, path
import django

sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_price.settings")
django.setup()

from project.models import *


def getGenre():
    # genre = {}
    # for make in Make.objects.all():
    #     make_name = make.name.lower().strip()
    #     genre[make_name] = {'alias': make.alias}
    #     for model in Model.objects.filter(make=make):
    #         year_filter = [{'from': item.from_year, 'to': item.to_year} for item in YearFilter.objects.filter(model=model)]
    #         model_name = model.name.lower().strip()

    #         genre[make_name][model_name] = {'alias': model.alias}
    #         genre[make_name][model_name]['year_filter'] = year_filter

    genre = {u'porsche': {u'911 targa': {'alias': u'911 Targa', 'year_filter': [{'to': 2100L, 'from': 1963L}]}, u'356': {'alias': u'356', 'year_filter': [{'to': 1965L, 'from': 1953L}]}, u'924': {'alias': u'924', 'year_filter': [{'to': 1988L, 'from': 1976L}]}, u'944': {'alias': u'944', 'year_filter': [{'to': 1991L, 'from': 1982L}]}, u'panamera': {'alias': u'Panamera', 'year_filter': [{'to': 2100L, 'from': 2009L}]}, u'968': {'alias': u'968', 'year_filter': [{'to': 1995L, 'from': 1992L}]}, u'cayenne': {'alias': u'Cayenne', 'year_filter': [{'to': 2100L, 'from': 2003L}]}, u'928': {'alias': u'928', 'year_filter': [{'to': 1995L, 'from': 1977L}]}, 'alias': u'Porsche', u'carrera gt': {'alias': u'Carrera GT', 'year_filter': [{'to': 2005L, 'from': 2004L}]}, u'boxster': {'alias': u'Boxster', 'year_filter': [{'to': 2100L, 'from': 1997L}]}, u'918': {'alias': u'918', 'year_filter': [{'to': 2016L, 'from': 2014L}]}, u'911 turbo': {'alias': u'911 Turbo', 'year_filter': [{'to': 2100L, 'from': 1975L}]}, u'cayman': {'alias': u'Cayman', 'year_filter': [{'to': 2100L, 'from': 2005L}]}, u'911 gt3': {'alias': u'911 GT3', 'year_filter': [{'to': 2100L, 'from': 1999L}]}, u'914': {'alias': u'914', 'year_filter': [{'to': 1976L, 'from': 1969L}]}, u'911': {'alias': u'911', 'year_filter': [{'to': 2100L, 'from': 1963L}]}, u'912': {'alias': u'912', 'year_filter': [{'to': 1976L, 'from': 1965L}]}}, u'lamborghini': {u'murcielago': {'alias': u'Murcielago', 'year_filter': [{'to': 2010L, 'from': 2002L}]}, u'gallardo': {'alias': u'Gallardo', 'year_filter': [{'to': 2014L, 'from': 2003L}]}, 'alias': u'Lamborghini', u'diablo': {'alias': u'Diablo', 'year_filter': [{'to': 2001L, 'from': 1990L}]}, u'huracan': {'alias': u'Huracan', 'year_filter': [{'to': 2100L, 'from': 2014L}]}, u'aventador': {'alias': u'Aventador', 'year_filter': [{'to': 2100L, 'from': 2011L}]}, u'countach': {'alias': u'Countach', 'year_filter': [{'to': 1990L, 'from': 1974L}]}}, u'jaguar': {'alias': u'Jaguar', u'e-type': {'alias': u'E-Type', 'year_filter': [{'to': 1975L, 'from': 1961L}]}, u'f-type': {'alias': u'F-Type', 'year_filter': [{'to': 2100L, 'from': 2013L}]}}, u'bentley': {u'flying spur': {'alias': u'Flying Spur', 'year_filter': [{'to': 2100L, 'from': 2005L}]}, u'continental gt': {'alias': u'Continental GT', 'year_filter': [{'to': 2100L, 'from': 2004L}]}, u'bentayga': {'alias': u'Bentayga', 'year_filter': [{'to': 2100L, 'from': 2016L}]}, u'arnage': {'alias': u'Arnage', 'year_filter': [{'to': 2009L, 'from': 1998L}]}, u'continental': {'alias': u'Continental', 'year_filter': [{'to': 1965L, 'from': 1952L}, {'to': 2100L, 'from': 1984L}]}, 'alias': u'Bentley', u'mulsanne': {'alias': u'Mulsanne', 'year_filter': [{'to': 1992L, 'from': 1980L}, {'to': 2100L, 'from': 2010L}]}, u'continental gtc': {'alias': u'Continental GTC', 'year_filter': [{'to': 2100L, 'from': 2007L}]}, u'continental flying spur': {'alias': u'Continental Flying Spur', 'year_filter': [{'to': 2100L, 'from': 2005L}]}, u'azure': {'alias': u'Azure', 'year_filter': [{'to': 2003L, 'from': 1995L}, {'to': 2010L, 'from': 2006L}]}, u'continental supersports': {'alias': u'Continental Supersports', 'year_filter': [{'to': 2013L, 'from': 2009L}]}, u'eight': {'alias': u'Eight', 'year_filter': [{'to': 1992L, 'from': 1984L}]}, u'brooklands': {'alias': u'Brooklands', 'year_filter': [{'to': 1998L, 'from': 1993L}, {'to': 2011L, 'from': 2008L}]}}, u'lotus': {u'exige': {'alias': u'Exige', 'year_filter': [{'to': 2100L, 'from': 2000L}]}, u'esprit': {'alias': u'Esprit', 'year_filter': [{'to': 2004L, 'from': 1976L}]}, 'alias': u'Lotus', u'elan': {'alias': u'Elan', 'year_filter': [{'to': 1975L, 'from': 1962L}, {'to': 1996L, 'from': 1989L}]}, u'elise': {'alias': u'Elise', 'year_filter': [{'to': 2100L, 'from': 1997L}]}, u'evora': {'alias': u'Evora', 'year_filter': [{'to': 2100L, 'from': 2010L}]}}, u'chevrolet': {u'corvette': {'alias': u'Corvette', 'year_filter': [{'to': 2100L, 'from': 1984L}]}, 'alias': u'Chevrolet', u'camaro': {'alias': u'Camaro', 'year_filter': [{'to': 2002L, 'from': 1967L}, {'to': 2100L, 'from': 2010L}]}}, u'nissan': {u'370z': {'alias': u'370Z', 'year_filter': [{'to': 2100L, 'from': 2009L}]}, 'alias': u'Nissan', u'350z': {'alias': u'350Z', 'year_filter': [{'to': 2009L, 'from': 2003L}]}, u'gt-r': {'alias': u'GT-R', 'year_filter': [{'to': 2100L, 'from': 2009L}]}, u'300zx': {'alias': u'300ZX', 'year_filter': [{'to': 2000L, 'from': 1983L}]}}, u'mclaren': {u'p1': {'alias': u'P1', 'year_filter': [{'to': 2016L, 'from': 2013L}]}, u'675lt': {'alias': u'675LT', 'year_filter': [{'to': 2100L, 'from': 2015L}]}, u'650s': {'alias': u'650S', 'year_filter': [{'to': 2100L, 'from': 2014L}]}, u'570s': {'alias': u'570S', 'year_filter': [{'to': 2100L, 'from': 2015L}]}, 'alias': u'McLaren', u'650s spider': {'alias': u'650S', 'year_filter': [{'to': 2100L, 'from': 2014L}]}}, u'aston martin': {u'rapide': {'alias': u'Rapide', 'year_filter': [{'to': 2100L, 'from': 2010L}]}, u'v12 vantage': {'alias': u'V12 Vantage', 'year_filter': [{'to': 2100L, 'from': 2011L}]}, u'virage': {'alias': u'Virage', 'year_filter': [{'to': 2012L, 'from': 2011L}]}, u'db9': {'alias': u'DB9', 'year_filter': [{'to': 2016L, 'from': 2004L}]}, 'alias': u'Aston Martin', u'rapide s': {'alias': u'Rapide', 'year_filter': [{'to': 2100L, 'from': 2010L}]}, u'v8 vantage': {'alias': u'V8 Vantage', 'year_filter': [{'to': 2100L, 'from': 2005L}]}, u'virage volante': {'alias': u'Virage', 'year_filter': [{'to': 2012L, 'from': 2011L}]}, u'dbs': {'alias': u'DBS', 'year_filter': [{'to': 2012L, 'from': 2008L}]}, u'db7': {'alias': u'DB7', 'year_filter': [{'to': 2004L, 'from': 1999L}]}, u'vanquish': {'alias': u'Vanquish', 'year_filter': [{'to': 2007L, 'from': 2001L}, {'to': 2100L, 'from': 2012L}]}}, u'tesla': {u'model x': {'alias': u'Model X', 'year_filter': [{'to': 2100L, 'from': 2016L}]}, 'alias': u'Tesla', u'model s': {'alias': u'Model S', 'year_filter': [{'to': 2100L, 'from': 2012L}]}, u'roadster': {'alias': u'Roadster', 'year_filter': [{'to': 2012L, 'from': 2008L}]}}, u'mercedes benz': {'alias': u'Mercedes-Benz', u'slr mclaren': {'alias': u'SLR-McLaren', 'year_filter': [{'to': 2010L, 'from': 2003L}]}, u'amg gt': {'alias': u'AMG GT-S', 'year_filter': [{'to': 2100L, 'from': 2014L}]}, u'sls amg': {'alias': u'SLS-AMG', 'year_filter': [{'to': 2015L, 'from': 2010L}]}}, u'ferrari': {u'enzo': {'alias': u'Enzo', 'year_filter': [{'to': 2005L, 'from': 2002L}]}, u'ff': {'alias': u'FF', 'year_filter': [{'to': 2016L, 'from': 2011L}]}, u'599': {'alias': u'599', 'year_filter': [{'to': 2012L, 'from': 2006L}]}, u'458 italia': {'alias': u'458', 'year_filter': [{'to': 2015L, 'from': 2010L}]}, u'456': {'alias': u'456', 'year_filter': [{'to': 2003L, 'from': 1993L}]}, u'f430': {'alias': u'F430', 'year_filter': [{'to': 2009L, 'from': 2005L}]}, u'458 spider': {'alias': u'458', 'year_filter': [{'to': 2015L, 'from': 2010L}]}, u'f40': {'alias': u'F40', 'year_filter': [{'to': 1993L, 'from': 1987L}]}, u'458 speciale': {'alias': u'458', 'year_filter': [{'to': 2015L, 'from': 2010L}]}, u'laferrari': {'alias': u'LaFerrari', 'year_filter': [{'to': 2100L, 'from': 2014L}]}, u'328': {'alias': u'328', 'year_filter': [{'to': 1989L, 'from': 1986L}]}, u'348': {'alias': u'348', 'year_filter': [{'to': 1995L, 'from': 1989L}]}, u'360': {'alias': u'360', 'year_filter': [{'to': 2005L, 'from': 1999L}]}, u'308': {'alias': u'308', 'year_filter': [{'to': 1985L, 'from': 1975L}]}, u'550': {'alias': u'550', 'year_filter': [{'to': 2002L, 'from': 1996L}]}, u'f355': {'alias': u'F355', 'year_filter': [{'to': 1999L, 'from': 1994L}]}, u'california': {'alias': u'California', 'year_filter': [{'to': 2100L, 'from': 2008L}]}, u'575': {'alias': u'575', 'year_filter': [{'to': 2006L, 'from': 2002L}]}, u'california t': {'alias': u'California', 'year_filter': [{'to': 2100L, 'from': 2008L}]}, u'488 gtb': {'alias': u'488', 'year_filter': [{'to': 2100L, 'from': 2015L}]}, u'mondial': {'alias': u'Mondial', 'year_filter': [{'to': 1994L, 'from': 1980L}]}, u'f50': {'alias': u'F50', 'year_filter': [{'to': 1997L, 'from': 1995L}]}, u'488 gts spider': {'alias': u'488', 'year_filter': [{'to': 2100L, 'from': 2015L}]}, 'alias': u'Ferrari', u'612 scaglietti': {'alias': u'612 Scaglietti', 'year_filter': [{'to': 2011L, 'from': 2004L}]}, u'512': {'alias': u'512', 'year_filter': [{'to': 1996L, 'from': 1974L}]}, u'testarossa': {'alias': u'Testarossa', 'year_filter': [{'to': 1996L, 'from': 1984L}]}}, u'bmw': {u'i8': {'alias': u'i8', 'year_filter': [{'to': 2100L, 'from': 2014L}]}, u'm4': {'alias': u'M4', 'year_filter': [{'to': 2100L, 'from': 2014L}]}, u'm5': {'alias': u'M5', 'year_filter': [{'to': 2100L, 'from': 1985L}]}, 'alias': u'BMW', u'm6 gran coupe': {'alias': u'M6', 'year_filter': [{'to': 1989L, 'from': 1984L}, {'to': 2010L, 'from': 2005L}, {'to': 2100L, 'from': 2012L}]}, u'm6': {'alias': u'M6', 'year_filter': [{'to': 1989L, 'from': 1984L}, {'to': 2010L, 'from': 2005L}, {'to': 2100L, 'from': 2012L}]}, u'z8': {'alias': u'Z8', 'year_filter': [{'to': 2003L, 'from': 2000L}]}, u'm3': {'alias': u'M3', 'year_filter': [{'to': 2100L, 'from': 2000L}]}, u'm2': {'alias': u'M2', 'year_filter': [{'to': 2100L, 'from': 2015L}]}, u'z1': {'alias': u'Z1', 'year_filter': [{'to': 1992L, 'from': 1989L}]}}, u'rolls royce': {u'ghost': {'alias': u'Ghost', 'year_filter': [{'to': 2100L, 'from': 2010L}]}, u'phantom': {'alias': u'Phantom', 'year_filter': [{'to': 2100L, 'from': 2004L}]}, u'corniche': {'alias': u'Corniche', 'year_filter': [{'to': 1995L, 'from': 1966L}]}, 'alias': u'Rolls Royce', u'silver seraph': {'alias': u'Silver Seraph', 'year_filter': [{'to': 2002L, 'from': 1998L}]}, u'wraith': {'alias': u'Wraith', 'year_filter': [{'to': 2100L, 'from': 2013L}]}, u'silver shadow': {'alias': u'Silver Shadow', 'year_filter': [{'to': 1980L, 'from': 1966L}]}, u'silver spirit': {'alias': u'Silver Spirit', 'year_filter': [{'to': 1999L, 'from': 1980L}]}}, u'maserati': {u'ghibli': {'alias': u'Ghibli', 'year_filter': [{'to': 2100L, 'from': 2013L}]}, u'gransport': {'alias': u'GranSport', 'year_filter': [{'to': 2008L, 'from': 2004L}]}, u'granturismo convertible': {'alias': u'GranTursimo', 'year_filter': [{'to': 2100L, 'from': 2007L}]}, u'coupe': {'alias': u'Coupe', 'year_filter': [{'to': 2007L, 'from': 2002L}]}, 'alias': u'Maserati', u'grantursimo': {'alias': u'GranTursimo', 'year_filter': [{'to': 2100L, 'from': 2007L}]}, u'levante': {'alias': u'Levante', 'year_filter': [{'to': 2100L, 'from': 2016L}]}, u'quattroporte': {'alias': u'Quattroporte', 'year_filter': [{'to': 2100L, 'from': 2004L}]}, u'spyder': {'alias': u'Spyder', 'year_filter': [{'to': 2007L, 'from': 2001L}]}}, u'audi': {u's8': {'alias': u'S8', 'year_filter': [{'to': 2100L, 'from': 1997L}]}, u'r8 spyder': {'alias': u'R8', 'year_filter': [{'to': 2100L, 'from': 2007L}]}, u's3': {'alias': u'S3', 'year_filter': [{'to': 2003L, 'from': 1999L}, {'to': 2100L, 'from': 2006L}]}, u's7': {'alias': u'S7', 'year_filter': [{'to': 2100L, 'from': 2012L}]}, u'r8': {'alias': u'R8', 'year_filter': [{'to': 2100L, 'from': 2007L}]}, u's6': {'alias': u'S6', 'year_filter': [{'to': 2100L, 'from': 1994L}]}, u's5': {'alias': u'S5', 'year_filter': [{'to': 2100L, 'from': 2007L}]}, u's4': {'alias': u'S4', 'year_filter': [{'to': 2100L, 'from': 1992L}]}, 'alias': u'Audi', u'rs4': {'alias': u'RS4', 'year_filter': [{'to': 2001L, 'from': 2000L}, {'to': 2008L, 'from': 2006L}, {'to': 2015L, 'from': 2012L}]}, u'rs5': {'alias': u'RS5', 'year_filter': [{'to': 2015L, 'from': 2010L}]}, u'rs6': {'alias': u'RS6', 'year_filter': [{'to': 2010L, 'from': 2002L}, {'to': 2016L, 'from': 2013L}]}, u'rs7': {'alias': u'RS7', 'year_filter': [{'to': 2100L, 'from': 2013L}]}, u'rs3': {'alias': u'RS3', 'year_filter': [{'to': 2013L, 'from': 2011L}, {'to': 2016L, 'from': 2015L}]}}}
    return genre


def save(item):
    car = Car.objects.filter(car_id=item["car_id"]).first()
    if car:
        car.prev_price = car.price
        car.price = item["price"]
        car.updated = 1
    else:
        car = Car(**item)
    car.save()


def setUpdateFlag():
    Car.objects.all().update(updated=0)


def removeNotCar():
    Car.objects.filter(updated=0).delete()
    