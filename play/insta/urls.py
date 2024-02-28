from django.urls import path
from . import views

# urlpatterns = [
#     path('',views.home),
#     path('home/',views.home1),
#     path('home1/',views.home2),
#     path('leo/',views.home3)
# ]

urlpatterns = [
    path('',views.home),
    path('welcome/',views.welcome),
    path('welcome/product/',views.product),
    path('pro/',views.pro),
    path('new/',views.new)
]