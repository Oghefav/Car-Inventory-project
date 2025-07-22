from rest_framework import serializers
from car.models import Car, CarAvailability, CarCondition, CarMake

class CarMakeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk',read_only=True)
    class Meta:
        model = CarMake
        fields = ['id', 'company_name', 'logo',]
    
class CarSerializer(serializers.ModelSerializer):
    condition = serializers.StringRelatedField()
    condition_id = serializers.PrimaryKeyRelatedField(queryset=CarCondition.objects.all(), write_only=True)
    availability_status= serializers.StringRelatedField(read_only=True)
    availability_status_id = serializers.PrimaryKeyRelatedField(queryset=CarAvailability.objects.all(), write_only=True)
    id = serializers.IntegerField(source='pk',read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    car_make = serializers.StringRelatedField(read_only=True)
    car_make_id = serializers.PrimaryKeyRelatedField(
        queryset=CarMake.objects.all(), write_only=True
    )

    class Meta:
        model = Car
        fields = ['id', 'car_model','car_make', 'car_make_id', 'year_of_manufacture','vehicle_identification_number', 'availability_status','availability_status_id', 'price', 'mileage', 'condition', 'condition_id', 'engine_type', 'transmission', 'number_of_doors', 'car_image', 'accident_history', 'created_at', 'updated_at', ]
    def create(self, validated_data):
        car_make = validated_data.pop('car_make_id')
        availability_status = validated_data.pop('availability_status_id')
        condition = validated_data.pop('condition_id')
        return Car.objects.create(car_make=car_make, availability_status=availability_status, condition=condition,**validated_data) 


    

class CarListSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Car
        fields = [ 'id','car_model','car_make', 'car_make_id', 'year_of_manufacture','vehicle_identification_number', 'availability_status','availability_status_id', 'price', 'mileage', 'condition', 'condition_id', 'engine_type', 'transmission', 'number_of_doors', 'car_image', 'accident_history', 'created_at', 'updated_at']


class CarAvailabilitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk',read_only=True)

    class Meta:
        model = CarAvailability
        fields = ['id', 'status_name']

class CarConditionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk',read_only=True)
    class Meta:
        model = CarCondition
        fields = ['id', 'condition']



class AvailableCarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk',read_only=True)
    car = CarListSerializer(many=True, read_only= True)

    class Meta:
        model = CarAvailability
        fields = ['id', 'status_name', 'car']
        # depth =1

class CarListCondition(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk',read_only=True)
    car = CarListSerializer(many=True, read_only=True)

    class Meta:
        model = CarCondition
        fields = ['id', 'condition', 'car']

class CarMakeListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk',read_only=True)
    car = CarListSerializer(many=True, read_only=True)

    class Meta:
        model = CarMake
        fields = ['id', 'company_name','logo', 'car']
