from rest_framework import serializers
from .models import Food, Category


class FoodSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Food
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
