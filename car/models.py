from django.db import models

# Create your models here.
class CarAvailability(models.Model):
    class AvaliabliltyChoices(models.TextChoices):
        IN_STOCK = 'in_stock', 'In_stock'
        SOLD = 'sold', 'Sold'
        RESERVED = 'reserved', 'Reserved'
        RENTED = 'rented', 'Rented'

    status_name = models.CharField(max_length=20,choices=AvaliabliltyChoices.choices)

    def __str__(self):
        return self.status_name
    
class CarCondition(models.Model):
    class ConditionChoices(models.TextChoices):
        NEW = 'new', 'New'
        USED = 'used', 'Used'
        CERTIFIED_PRE_OWNED = 'certified_pre_owned', 'Certified_pre_owned'

    condition = models.CharField(max_length=20,choices=ConditionChoices.choices)

    def __str__(self):
        return self.condition
    
class CarMake(models.Model):
    company_name = models.CharField(max_length=30, )
    logo = models.ImageField(upload_to="car_logo", null=False, blank=True)

    def __str__(self):
        return self.company_name
    
class EngineTypeChoice(models.TextChoices):
        PETROL = 'petrol', 'Petrol'
        DIESEL = 'diesel', 'Diesel'
        ELECTRIC = 'electric', 'Electric'
        HYBRID = 'hybrid', 'Hybrid'
        GAS = 'gas', 'Gas'

class TransmissionChoice(models.TextChoices):
    MANUAL = 'manual', 'Manual'
    AUTOMATIC = 'automatic', 'Automatic'
    CVT = 'cvt', 'CVT'


    
class Car(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name= 'car')
    car_model = models.CharField(max_length=30, null=False, blank=True)
    year_of_manufacture = models.PositiveIntegerField()
    vehicle_identification_number = models.CharField(max_length=17, unique=True,)
    availability_status = models.ForeignKey(CarAvailability, on_delete=models.CASCADE, related_name='car')
    price = models.CharField(max_length=11)
    mileage = models.IntegerField()
    condition = models.ForeignKey(CarCondition, on_delete=models.CASCADE, related_name='car')
    engine_type = models.CharField(max_length=20, choices= EngineTypeChoice.choices, blank=True, null=True)
    transmission = models.CharField(max_length=20, choices=TransmissionChoice.choices)
    number_of_doors = models.PositiveSmallIntegerField()
    car_image= models.ImageField(upload_to='car_images', blank=True, null=True)
    accident_history = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.car_model} {self.car_make.company_name}"
    
    class Meta:
        ordering = ('-created_at',)