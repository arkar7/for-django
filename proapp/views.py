import collections

import pymongo
from django.shortcuts import render
from django.http import HttpResponse
from pymongo import collection


##Create your view here.
def home(request):
    return render(request, 'home.html')


def location(request):
    print(request.POST)
    return render(request, "success.html")


#################################################
import pymongo
from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from pymongo import collection

connection = pymongo.MongoClient("localhost",27017)
database = connection["MyDatabase"]
collection =database["MyDB"]

def home(request):
     try:
         data = collection.find_one()
         id,name,email,phnumber=data['_id'],data['name'],data['email'],data['phnumber']
         for i in data:
             print(i)

         return  render(request,'home.html',{'_id':id,'name':name,'email':email,'phnumber':phnumber,})
     except Exception as error:
         return render(request,'home.html',{'error':error})

     # try:
     #     data = collections.find({}, {"_id": 1, "name": 'arkar', "phnumber": 123456})
     #     for i in data:
     #         print(i)
     # except Exception as err:
     #     print(err)
