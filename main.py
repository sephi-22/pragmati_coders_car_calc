
from calculators import *

def monthly_loan_payment(interest_rate,principal,down_payment,years):
    amount_owed = principal-down_payment
    monthly_interest_rate = (interest_rate/100)/12
    monthly_payment = (amount_owed*monthly_interest_rate)/(1-(1+monthly_interest_rate)**(-years*12))
    print (monthly_payment)

print("Welcome to the car loan cost calculator. We have the following Cars in our database. Please pick one of these when entering a car model:")
print("")
for key, value in maintenance_costs.items():
    print(key,end=", ")
print("")
gas_price = get_gas_prices()
print("These are the current gas prices in your state")

for key, value in gas_price.items():
    print(key.capitalize(),": $",value)

number_of_comparisons = int(input("Enter the number of cars you'd like to compare: "))

total_costs = {}
for i in range(number_of_comparisons):
    car_brand=input("Enter the brand of the car:").lower()
    if car_brand not in maintenance_costs.keys():
        print("Car brand not recognized.")
        break
    months_to_75k, monthly_gas_cost = get_car_mileage(gas_price)
    monthly_maintenance_cost = get_monthly_maintenance_costs(months_to_75k,car_brand)
    monthly_interest_payment = get_monthly_interest_payment()
    total_monthly_payment = monthly_gas_cost + monthly_maintenance_cost + monthly_interest_payment
    total_costs[car_brand] = total_monthly_payment
    print(f"You will incur a monthly maintainance cost of: ${monthly_maintenance_cost:.2f}")
    print(f"You will incur a monthly gas cost of: ${monthly_gas_cost:.2f}")
    print(f"You will incur a monthly interest payment of: ${monthly_interest_payment:.2f}")
    print(f"The {car_brand} will cost you a total of ${total_monthly_payment:.2f} each month")

print("The total price breakdown of monthly costs for all cars is:")
for key, value in total_costs.items():
    print(key.capitalize(),": $",value)
print("The cheapest car based on monthly payments is the", min(total_costs, key=total_costs.get))
