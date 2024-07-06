month = input()
number_of_hours = int(input())
people_count = int(input())
time_of_day = input()
price_per_person = 0
total_for_person = 0
total_price_for_group = 0

if time_of_day == "day":
    if month in ["march", "april", "may"]:
        price_per_person = 10.50

        if people_count >= 4:
            price_per_person *= 0.90
        if number_of_hours >= 5:
            price_per_person *= 0.50

    elif month in ["june", "july", "august"]:
        price_per_person = 12.60
        if people_count >= 4:
            price_per_person *= 0.90
        if number_of_hours >= 5:
            price_per_person *= 0.50

    total_price_for_group = price_per_person * people_count * number_of_hours

elif time_of_day == "night":
    if month in ["march", "april", "may"]:
        price_per_person = 8.40

        if people_count >= 4:
            price_per_person *= 0.90
        if number_of_hours >= 5:
            price_per_person *= 0.50

    elif month in ["june", "july", "august"]:
        price_per_person = 10.20
        if people_count >= 4:
            price_per_person *= 0.90

        if number_of_hours >= 5:
            price_per_person *= 0.50

    total_price_for_group = price_per_person * people_count * number_of_hours

print(f"Price per person for one hour: {price_per_person:.2f}")
print(f"Total cost of the visit: {total_price_for_group:.2f}")
