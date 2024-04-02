from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="headlines"),
    path('sports',views.index1,name="sports"),
    path('trending',views.index2,name="trending"),
    path('top',views.index3,name="top"),
    path('entertainment',views.index4,name="entertainment"),
    path('science',views.index5,name="science")
]