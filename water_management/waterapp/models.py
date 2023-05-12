from django.db import models

class WaterManagement(models.Model):
    total_water_consumed = models.IntegerField()
    total_cost = models.IntegerField()
    allot_water = models.CharField(max_length=10, null=True, blank=True)
    num_guests = models.IntegerField(default=0)
    total_water_consumed = models.IntegerField(default=0)
    total_cost = models.IntegerField(default=0)

    def allot_water(self, apartment_type, ratio):
        pass
        
    def add_guests(self, num_guests):
        self.num_guests += num_guests
        self.save()

    def calculate_cost(self):
        pass
            
    def save(self, *args, **kwargs):
        self.calculate_cost()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Water Management - Consumption:({self.pk}) {self.total_water_consumed} | Cost: {self.total_cost}"
