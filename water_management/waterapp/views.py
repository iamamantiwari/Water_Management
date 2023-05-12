from django.shortcuts import render
from django.http import HttpResponse
from .models import WaterManagement

def water_management_view(request):
    water_manager = WaterManagement()

    commands = [
        "ALLOT_WATER 2 3:7",
        "ADD_GUESTS 2",
        "ADD_GUESTS 3",
        "BILL"
    ]

    for command in commands:
        command_parts = command.split()
        if command_parts[0] == "ALLOT_WATER":
            apartment_type = int(command_parts[1])
            ratio = command_parts[2]
            water_manager.allot_water(apartment_type, ratio)
        elif command_parts[0] == "ADD_GUESTS":
            num_guests = int(command_parts[1])
            water_manager.add_guests(num_guests)
        elif command_parts[0] == "BILL":
            water_manager.calculate_cost()

            # Create a WaterManagement object and save it to the database
            water_management_obj = WaterManagement(
                total_water_consumed=water_manager.total_water_consumed,
                total_cost=water_manager.total_cost
            )
            water_management_obj.save()

            return HttpResponse(f"{water_manager.total_water_consumed} {water_manager.total_cost}")

    return HttpResponse("Water management completed.")
