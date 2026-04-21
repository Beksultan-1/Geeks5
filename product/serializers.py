from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = 'id name products_count'.split()

    def get_products_count(self, obj):
        return obj.products.count()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()

class ProductSerializer(serializers.ModelSerializer): # Проверь это название!
    class Meta:
        model = Product
        fields = '__all__'

class ProductReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id title reviews rating'.split()

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if not reviews:
            return 0
        return sum([review.stars for review in reviews]) / reviews.count()
