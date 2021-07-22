from rest_framework import generics
from rest_framework.response import Response
from .serialize import CarSerialize, DealerSerialize
from .models import Car, Dealer

class CarCreateAPI(generics.CreateAPIView):
	queryset = Car.objects.all()
	serializer_class = CarSerialize

class CarAPI(generics.ListAPIView):
	queryset = Car.objects.all()
	serializer_class = CarSerialize

class CarUpdateAPI(generics.RetrieveUpdateAPIView):
	queryset = Car.objects.all()
	serializer_class = CarSerialize

class CarDeleteAPI(generics.RetrieveDestroyAPIView):
	queryset = Car.objects.all()
	serializer_class = CarSerialize

class DealerCreateAPI(generics.CreateAPIView):
	queryset = Dealer.objects.all()
	serializer_class = DealerSerialize

class DealerAPI(generics.ListAPIView):
	queryset = Dealer.objects.all()
	serializer_class = DealerSerialize

class DealerUpdateAPI(generics.RetrieveUpdateAPIView):
	queryset = Dealer.objects.all()
	serializer_class = DealerSerialize

class DealerDeleteAPI(generics.RetrieveDestroyAPIView):
	queryset = Dealer.objects.all()
	serializer_class = DealerSerialize