from rest_framework import serializers

from .models import Car, Dealer

class CarSerialize(serializers.ModelSerializer):
	class Meta:
		model = Car
		fields = '__all__'

class DealerSerialize(serializers.ModelSerializer):
	class Meta:
		model = Dealer
		fields = '__all__'