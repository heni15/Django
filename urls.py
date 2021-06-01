from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name=""),
    path('shop',views.shop,name="shop"),
    path('vetrine',views.vetrine,name="vetrine"),
    path('forni',views.forni,name="forni"),
    path('forniprod/<id>',views.forniprod,name="forniprod"),
    path('viewshop',views.viewshop,name="viewshop"),
    path('viewshopcard/<id>',views.viewshopcard,name="viewshopcard"),
]