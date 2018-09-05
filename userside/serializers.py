from rest_framework import fields, serializers
from .models import Vehicle, Shop
from userside.models import SERVICE_CHOICES


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'

class ShopSerializer(serializers.HyperlinkedModelSerializer):

    services = fields.MultipleChoiceField(choices=SERVICE_CHOICES)

    class Meta:
        model = Shop
        fields = ('id', 'logo', 'name', 'type', 'phone', 'services', 'address', 'city', 'lat', 'long', 'isActive')



