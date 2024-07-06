kids = 0
adults = 0
toy_price = 5
sweaters_price = 15
toy_cout = 0
sweaters_count = 0
total = 0
age = ''
while age != "Christmas":
    age = input()

    if age == "Christmas":
        break
    elif age == "":
        break
    else:
        age = int(age)
        if age <= 16:
            kids += 1
        else:
            adults += 1
print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {kids * toy_price}")
print(f"Money for sweaters: {adults * sweaters_price}")
