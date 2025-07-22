from rest_framework import viewsets,status
from datetime import datetime
from rest_framework.parsers import MultiPartParser, FileUploadParser
from car.permissions import IsAdminOrReadOnly
from car.models import Car,CarAvailability, CarCondition, CarMake
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from car.serializer import CarAvailabilitySerializer, CarConditionSerializer, CarMakeListSerializer, CarSerializer, AvailableCarSerializer, CarMakeSerializer, CarListCondition

class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    http_method_names = ['get', 'put', 'patch', 'post', 'delete']
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = [MultiPartParser, FileUploadParser]

    def get_queryset(self):
        cars = Car.objects.all()
        return cars
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'New car has been created'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['get'], detail=False)
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'start', openapi.IN_QUERY,
                description="Start date in YYYY-MM-DD",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'end', openapi.IN_QUERY,
                description="End date in YYYY-MM-DD",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
    def get_car_by_date_range(self, request): 
        start = request.query_params.get('start')
        end = request.query_params.get('end')

        if not start or not end:
            return Response({'error': 'Provide both start and end date in YYYY-MM-DD format'})

        try:
            start_date = datetime.strptime(start, '%Y-%m-%d')
            end_date = datetime.strptime(end, '%Y-%m-%d')
            car_objects = Car.objects.filter(created_at__range=(start_date, end_date))
            serializer = self.serializer_class(car_objects, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response({'message': 'Invalid date format. Use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)

    
class CarAvailablilityViewSet(viewsets.ModelViewSet):
    serializer_class = CarAvailabilitySerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = [MultiPartParser]


    def get_queryset(self):
        availability_status = CarAvailability.objects.all()
        return availability_status
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'message' : 'new availiability status have been added'
            },status=status.HTTP_201_CREATED)
        
class CarConditionViewSet(viewsets.ModelViewSet): 
    serializer_class = CarConditionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        car_conditions = CarCondition.objects.all()
        return car_conditions
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message' : 'new car condition have been created'}, status=status.HTTP_201_CREATED)
        
class CarMakeViewSet(viewsets.ModelViewSet):
    serializer_class = CarMakeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        car_makes = CarMake.objects.all()
        return car_makes
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message' : 'New car make has been created'}, status=status.HTTP_201_CREATED)
        
class CarMakeListViewSet(viewsets.ModelViewSet):
    serializer_class = CarMakeListSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return CarMake.objects.all()
    
class CarConditionListViewSet(viewsets.ModelViewSet):
    serializer_class = CarListCondition
    http_method_names = ['get']
    permission_classes = [AllowAny]

    def get_queryset(self):
        return CarCondition.objects.all()
    
class AvailableCarListViewSet(viewsets.ModelViewSet):
    serializer_class = AvailableCarSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return CarAvailability.objects.all()
    
    
