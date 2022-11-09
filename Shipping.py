weight = 3.3
# Ground shipping
if weight <= 2:
    ground_price = weight * 1.50 + 20
elif weight <= 6:
    ground_price = weight * 3.00 + 20
elif weight <= 10:
    ground_price = weight * 4.00 + 20
else:
    ground_price = weight * 4.75 + 20
print(ground_price)

# Ground Shipping Premium
ground_premium = 125

# Drone Shipping

if weight <= 2:
    drone_ship = weight * 4.50
elif weight <= 6:
    drone_ship = weight * 9.00
elif weight <= 10:
    drone_ship = weight * 12.00
else:
    drone_ship = weight * 14.25

print(ground_premium)

print(drone_ship)