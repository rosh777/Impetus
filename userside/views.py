from rest_framework import viewsets
from .models import Vehicle, Shop
from .serializers import VehicleSerializer, ShopSerializer

# List all vehicles or create one
# vehicles/
class Vehicle(viewsets.ModelViewSet):

    # def get(self, request):
    #     vehicles = Vehicle.objects.all()
    #     serializer = VehicleSerializer(vehicles, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class Shop(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


