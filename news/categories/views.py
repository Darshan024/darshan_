import requests
from django.shortcuts import render
import requests
def index(request):
    records6={}
    url=requests.get("https://inshorts.me/news/all?offset=0&limit=21")
    inshorts_data = url.json()
    records6['all']=inshorts_data
    return render(request,'home.html',records6)

def index1(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=sports")
    inshorts_data = url.json()
    records['sports'] = inshorts_data
    return render(request,'sports.html',records)

def index2(request):
    records1 = {}
    url = requests.get("https://inshorts.me/news/trending?offset=0&limit=21")
    inshorts_data = url.json()
    records1['trending'] = inshorts_data
    return render(request,'trending.html',records1)

def index3(request):
    records2 = {}
    url = requests.get("https://inshorts.me/news/top?offset=0&limit=21")
    inshorts_data = url.json()
    records2['top'] = inshorts_data
    return render(request,'top.html',records2)

def index4(request):
    records3 = {}
    url = requests.get("https://inshorts.me/news/topics/entertainment")
    inshorts_data = url.json()
    records3['entertainment'] = inshorts_data
    return render(request,'entertainment.html',records3)

def index5(request):
    records4 = {}
    url = requests.get("https://inshorts.me/news/topics/science")
    inshorts_data = url.json()
    records4['science'] = inshorts_data
    return render(request,'science.html',records4)