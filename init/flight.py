import os
os.system('clear')

total_distance = 30        # km
total_time = 45            # min

speed_first = 15           # km/h
time_first = 20            # min

distance_first = speed_first * (time_first / 60)  # km
distance_remaining = total_distance - distance_first
time_remaining = total_time - time_first           # min

speed_required = distance_remaining / (time_remaining / 60)  # km/h

print(f"Distance covered in first {time_first} min: {distance_first} km")
print(f"Distance remaining: {distance_remaining} km")
print(f"Time remaining: {time_remaining} min")
print(f"Required average speed: {speed_required} km/h")
print("")

