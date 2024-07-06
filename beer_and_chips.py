import math

beer_price = 1.20

football_fan_name = input()
budget = float(input())
purchased_beers = int(input())
chips_bags = int(input())
total_beer = purchased_beers * beer_price
chips_price = total_beer * 0.45
total_chips_price = math.ceil(chips_bags * chips_price)

total_cost = total_beer + total_chips_price

if total_cost <= budget:
    remaining_money = budget - total_cost
    print(f"{football_fan_name} bought a snack and has {remaining_money:.2f} leva left.")
else:
    needed_money = total_cost - budget
    print(f"{football_fan_name} needs {needed_money:.2f} more leva!")
    