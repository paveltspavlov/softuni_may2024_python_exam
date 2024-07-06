number_of_locations = int(input())

while number_of_locations > 0:
    average_gold = float(input())
    days = int(input())
    total_gold_mined = 0

    for _ in range(days):
        gold_mined = float(input())
        total_gold_mined += gold_mined

    average_gold_digged = total_gold_mined / days

    if average_gold_digged >= average_gold:
        print(f"Good job! Average gold per day: {average_gold_digged:.2f}.")
    else:
        print(f"You need {average_gold - average_gold_digged:.2f} gold.")

    number_of_locations -= 1
