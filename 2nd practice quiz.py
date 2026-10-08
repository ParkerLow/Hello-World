# Parker Low
# 09/16/2026
# practice quiz 2 - chat made

import math

hours_parked = float(input("Enter number of hours parked: "))

base_cost = 18
additional_hour_cost = 6


if hours_parked > 3:
    additional_hours = math.ceil(hours_parked - 3)
    additional_cost = additional_hours * additional_hour_cost
else:
    additional_hours = 0
    additional_cost = 0


total_cost = base_cost + additional_cost

print("Hours parked: ", hours_parked)
print("Additional hours: ", additional_hours)
print("Additional cost: ", round(additional_cost, 2))
print("Total cost: ", round(total_cost, 2))


# 2

person_type = input("Are you a student, adult, or senior: ")
person_membership = input(" Are you a memeber: Yes/No: ")

daypass_fee = 0

if person_type == "student":
    daypass_fee = 20
elif person_type == "adult":
    daypass_fee = 35
elif person_type == "senior":
    daypass_fee = 25
else:
    print("Invalid Pass Type.")

if daypass_fee > 0:
    if person_membership == "Yes":
        discount = daypass_fee * 0.30
    else:
        discount = 0

    total_cost = daypass_fee - discount

    print("Pass type: ", person_type)
    print("Base fee: ", daypass_fee)
    print("Discount amount: ", round(discount, 2))
    print(" Amount due: ", round(total_cost, 2))
