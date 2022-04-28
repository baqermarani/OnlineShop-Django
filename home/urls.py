from django.urls import path, include
from . import views

app_name = 'home'

bucket_urls = [
    path('bucket/', views.BucketHome.as_view(), name='bucket'),
	path('delete_bucket/<str:key>',views.DeleteBucket.as_view(), name='bucket_delete'),
]

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('bucket/', include(bucket_urls)),
    path('<slug:slug>/',views.ProductDetailView.as_view(), name='product_detail'),
]