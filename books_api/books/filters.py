from django_filters import rest_framework as filters
from .models import Book


# We create filters for each field we want to be able to filter on
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    desc = filters.CharFilter(field_name='description', lookup_expr='icontains')
    publisher = filters.CharFilter(lookup_expr='icontains')
    year = filters.NumberFilter()
    year__gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    year__lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    author = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'desc', 'publisher', 'year', 'year__gt', 'year__lt', 'author']
