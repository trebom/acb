from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        # fields = ("name","kind")
        # fields = "__all__"
        # exclude =("create_at")