from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ссылки для категорий
    path('api/v1/categories/', views.category_list_view),
    path('api/v1/categories/<int:id>/', views.category_detail_view),

    # Ссылка для товаров с отзывами 
    path('api/v1/products/reviews/', views.products_reviews_view),

    # Ссылки для товаров
    path('api/v1/products/', views.product_list_view),
    path('api/v1/products/<int:id>/', views.product_detail_view),

    # Ссылки для отзывов
    path('api/v1/reviews/', views.review_list_view),
    path('api/v1/reviews/<int:id>/', views.review_detail_view),
]