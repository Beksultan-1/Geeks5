from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = 'id name products_count'.split()

    def get_products_count(self, obj):
        return obj.products.count()

    # Валидация для имени категории
    def validate_name(self, name):
        if len(name) < 3:
            raise ValidationError("Название категории должно быть длиннее 3 символов!")
        return name

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars product'.split()

    # Валидация для текста отзыва
    def validate_text(self, text):
        if not text:
            raise ValidationError("Отзыв не может быть пустым!")
        return text

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # Валидация для цены
    def validate_price(self, price):
        if price <= 0:
            raise ValidationError("Цена должна быть больше нуля!")
        return price

    # Валидация для названия товара
    def validate_title(self, title):
        if len(title) > 100:
            raise ValidationError("Слишком длинное название!")
        return title

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
