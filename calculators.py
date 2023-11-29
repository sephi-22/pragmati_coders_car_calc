from get_gas_prices import *
from car_maintenance_costs import maintenance_costs

url = "https://gasprices.aaa.com/state-gas-price-averages/"
gas_prices = scrape_for_gas_prices(url)

def get_gas_prices():
    user_state = input("Enter your state:").capitalize()
    if user_state in gas_prices:
        state_prices = gas_prices[user_state]
    return state_prices

def get_user_miles():
    city_miles_weekday = float(input("How many miles would you drive in the city during M-F on average: "))
    city_miles_weekend = float(input("How many miles would you drive in the city during Sat/Sun on average?: "))
    hway_miles_weekday = float(input("How many miles would you drive on highways during M-F on average: "))
    hway_miles_weekend = float(input("How many miles would you drive on highways during Sat/Sun on average?: "))
    city_miles_month = (city_miles_weekday*5 + city_miles_weekend*2)*52/12
    hway_miles_month = (hway_miles_weekday*5 + hway_miles_weekend*2)*52/12
    total_miles_month = city_miles_month + hway_miles_month
    months_to_75k = 75000/total_miles_month
    return city_miles_month, hway_miles_month, months_to_75k

def get_car_mileage(state_prices,city_miles_month,hway_miles_month):
    fuel_type = input("Enter the fuel type of the car (Regular/Midgrade/Premium/Diesel): ").capitalize()
    cost_per_gallon = 0  
    if fuel_type in state_prices:
        cost_per_gallon = float(state_prices[fuel_type])
    city_mileage = float(input("Enter the city mileage of the car:"))
    hway_mileage = float(input("Enter the highway mileage of the car:"))
    monthly_gas_cost = (city_miles_month/city_mileage)*cost_per_gallon + (hway_miles_month/hway_mileage)*cost_per_gallon
    return monthly_gas_cost
    
def get_monthly_maintenance_costs(months_to_75k, car_brand):
    return maintenance_costs[car_brand]/months_to_75k

def get_monthly_interest_payment():
    principal = float(input("Enter the Total price of the car/loan: "))
    down_payment = float(input("Enter the down payment on the car, 0 if no down payment: "))
    interest_rate = float(input("Enter the interest rate of the loan (yearly): "))
    years = float(input("Enter the loan duration in years: "))
    tax = float(input("Enter the sales tax rate for the purchase: "))

    amount_owed = principal + principal*tax/100 - down_payment
    monthly_interest_rate = (interest_rate/100)/12
    if monthly_interest_rate == 0:
        monthly_payment = amount_owed/(years*12)
    else:
        monthly_payment = (amount_owed*monthly_interest_rate)/(1-(1+monthly_interest_rate)**(-years*12))
    return monthly_payment