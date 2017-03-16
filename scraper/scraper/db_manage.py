#!/usr/bin/python
import os
from os import sys, path
import django

sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_price.settings")
django.setup()

from project.models import *
from django.db.models import Q, Avg, Count

def getBlocks():
    blocks = Block.objects.all()
    blocks = [item.car_id for item in blocks]
    for block in blocks:
        Car.objects.filter(car_id=block).delete()

    return blocks

def getGenre():
    genre = {}
    for make in Make.objects.all():
        make_name = make.name.lower().strip()
        genre[make_name] = {'alias': make.alias}
        for model in Model.objects.filter(make=make):
            year_filter = [{'from': item.from_year, 'to': item.to_year} for item in YearFilter.objects.filter(model=model)]
            model_name = model.name.lower().strip()

            genre[make_name][model_name] = {'alias': model.alias}
            genre[make_name][model_name]['name'] = model.name
            genre[make_name][model_name]['year_filter'] = year_filter
            genre[make_name][model_name]['min_price'] = model.min_price
            genre[make_name][model_name]['max_price'] = model.max_price
            genre[make_name][model_name]['year_interval'] = model.year_interval

    return genre
    

def save(item):
    car = Car.objects.filter(car_id=item["car_id"], updated=0).first()
    if car:
        car.prev_price = car.price
        car.price = item["price"]
        car.updated = 1
    else:
        car = Car(**item)
    car.save()


def setUpdateFlag():
    Car.objects.all().update(updated=0)       ##@@##

def updateAlias(model, alias):
    Car.objects.filter(brand=model).update(brand=alias)

def removeNotCar():
    cars = Car.objects.filter(updated=0)
    for car in cars:
        car.prev_price = car.price
        car.updated = 1
        car.price = 0
        car.save()

    Car.objects.filter(price=0, prev_price=0).delete()    ##@@##
    removeduplicatedCars()

def removeduplicatedCars():
    print "pp"
    cars = Car.objects.all().values('car_id').annotate(count=Count('price'))
    for car in cars:
        if car["count"] > 1:
            print car["car_id"]
            extra = Car.objects.filter(car_id=car["car_id"])[:1]
            pk_list = [item.id for item in extra]
            Car.objects.filter(car_id=car["car_id"]).exclude(pk__in=pk_list).delete() 

def checkBlocker():
    blocks = Block.objects.all()
    for block in blocks:
        if len(Car.objects.filter(car_id=block.car_id)) > 0:
            print block.car_id

