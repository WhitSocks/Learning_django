from django.db import models
from django.utils import timezone

class Drone(models.Model):
    serial_number = models.CharField(max_length=100,unique=True)
    model = models.CharField(max_length=20, choices=[('Lightweight', 'Lightweight'), ('Middleweight', 'Middleweight'), ('Cruiserweight', 'Cruiserweight'), ('Heavyweight', 'Heavyweight')])
    weight_limit = models.FloatField()
    battery_capacity = models.IntegerField()
    state = models.CharField(max_length=20, choices=[('IDLE', 'IDLE'), ('LOADING', 'LOADING'), ('LOADED', 'LOADED'), ('DELIVERING', 'DELIVERING'), ('DELIVERED', 'DELIVERED'), ('RETURNING', 'RETURNING')])

    def __str__(self):
        return f"Drone {self.serial_number}"

class Medication(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    code = models.CharField(max_length=20)
   

    def __str__(self):
        return self.name

class DroneMedication(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    loaded_timestamp = models.DateTimeField(default=timezone.now)
    delivered_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Drone {self.drone.serial_number} loaded with {self.medication.name}"
    
class BatteryLog(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    battery_level = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Battery Log for {self.drone} at {self.timestamp}"


# Create your models here.
