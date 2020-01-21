premium_shipping = 125
def ground_shipping(weight):
  if weight <= 2:
    return weight * 1.5 + 20
  elif weight > 2 and weight <= 6:
    return weight * 3 + 20
  elif weight > 6 and weight <= 10:
    return weight * 4 + 20
  else:
    return weight * 4.75 + 20

def drone_shipping(weight):
  if weight <= 2:
    return weight * 4.5
  elif weight > 2 and weight <= 6:
    return weight * 9
  elif weight > 6 and weight <= 10:
    return weight * 12
  else:
    return weight * 14.25
print(ground_shipping())
print(drone_shipping())

def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight):
    return "Ground Shipping : " + str(ground_shipping(weight))
  else:
    return "Drone Shipping : " + str(drone_shipping(weight))
  
print(cheapest_shipping())  
