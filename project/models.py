from __future__ import unicode_literals

from django.db import models


class Car(models.Model):
    car_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.IntegerField()
    prev_price = models.IntegerField()
    updated_on = models.DateField(auto_now=True)
    updated = models.IntegerField(default=1)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'CarPrice'


class Make(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)

    def __unicode__(self):
        return self.alias

    class Meta:
        ordering = ('name',)


class Model(models.Model):
    
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    make = models.ForeignKey(Make)
    max_price = models.IntegerField(default=4500000)
    min_price = models.IntegerField(default=3500)    
    year_interval = models.IntegerField(default=0)    

    def __unicode__(self):
        return "{} - {} - {}".format(self.make.alias, self.alias, self.name)

    class Meta:
        ordering = ('make__alias', 'name')


class YearFilter(models.Model):
    model = models.ForeignKey(Model)
    from_year = models.IntegerField('From')
    to_year = models.IntegerField('To')

    def __unicode__(self):
        return "{} : {}-{}".format(self.model.alias, self.from_year, self.to_year)

class Price(models.Model):
    model = models.ForeignKey(Model)
    usa_low_price = models.IntegerField('USA Low Price', blank=True, null=True)
    usa_avg_price = models.IntegerField('USA Average Price', blank=True, null=True)
    usa_high_price = models.IntegerField('USA High Price', blank=True, null=True)

    uk_low_price = models.IntegerField('UK Low Price', blank=True, null=True)
    uk_avg_price = models.IntegerField('UK Average Price', blank=True, null=True)
    uk_high_price = models.IntegerField('UK High Price', blank=True, null=True)
    
    year = models.IntegerField('Year')

    # def __unicode__(self):
    #     return "{} : {}-{}-{}-{}".format(self.model.alias, self.year, self.low_price, self.avg_price, self.high_price)        

class Block(models.Model):
    car_id = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'Block'

