from rest_framework import routers
from car.viewset import CarAvailablilityViewSet, CarConditionListViewSet, CarConditionViewSet, CarMakeListViewSet, CarMakeViewSet, CarViewSet, AvailableCarListViewSet

router = routers.DefaultRouter()

router.register(r'car', CarViewSet, basename='Car')
router.register(r'avaliable_cars', AvailableCarListViewSet, basename='Available Cars')
router.register(r'car_condition_list', CarConditionListViewSet, basename='Car Condition list')
router.register(r'car_condition', CarConditionViewSet, basename='Car Condition')
router.register(r'car_avalibility_status', CarAvailablilityViewSet, basename='Car Availability Status')
router.register(r'car_make_list', CarMakeListViewSet, basename= 'Car Make List')
router.register(r'car_make', CarMakeViewSet, basename='Car Make')

urlpatterns = [
    *router.urls
]