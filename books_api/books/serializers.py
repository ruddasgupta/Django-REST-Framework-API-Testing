import datetime

from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        if attrs['year'] > datetime.date.today().year:
            raise serializers.ValidationError({"year": "Must be <= current year"})
        elif attrs['year'] < 0:
            raise serializers.ValidationError({"year": "Must be +"})
        return attrs
