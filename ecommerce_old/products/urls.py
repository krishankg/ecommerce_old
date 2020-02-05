from django.urls import path
from . import views
app_name='products'
urlpatterns=[
       path('',views.ProductListView.as_view(),name='list'),
       # path('detail/<int:pk>/',views.ProductDetailView.as_view(),name='detail'),
       path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='detail'),

       # path('products-fbv/',views.product_list_view),
       # path('products/',views.ProductListView.as_view())

]