from rest_framework import serializers
from . import models

from django_measurement.models import MeasurementField
from measurement.measures import Volume, Area, Mass, Time, Weight

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ('user', 'product', 'rating')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('product_id','product_name', 'product_price', 'product_description')

# class ProductMeasurementsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.ProductMeasurements
#         fields = ('product_volume', 'product_area', 'product_mass', 'product_weight', 'product_time')

class ProductMeasurementsSerializer(serializers.Serializer):
    class Meta:
        model = models.ProductMeasurements
        field = ('product_volume')

class ProductMeasurementsListSerializer(serializers.ListSerializer):
    child =  ProductMeasurementsSerializer()