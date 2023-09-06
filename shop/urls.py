from django.urls import path , include
from . import views 

app_name = 'shop'

urlpatterns = [
    path('',views.product_list, name='product_list'),
    path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    # path('/test',views.view_name,name='view_name')
]