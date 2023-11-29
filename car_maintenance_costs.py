#Taken from: https://www.crsautomotive.com/what-are-the-total-costs-of-vehicle-ownership-per-brand/
#Maintenance costs per 75,000 miles
maintenance_costs = {
    "Hyundai": 4000,
    "Kia": 4000,
    "Toyota": 4300,
    "Nissan": 4600,
    "Subaru": 4700,
    "Scion": 4800,
    "Mazda": 4900,
    "Honda": 4900,
    "Volkswagen": 5600,
    "Acura": 5700,
    "Lexus": 5700,
    "Infiniti": 5800,
    "Jeep": 6500,
    "Mini": 6500,
    "GMC": 6600,
    "Dodge": 6700,
    "Mitsubishi": 7000,
    "Chevrolet": 7000,
    "Ford": 7900,
    "Buick": 8100,
    "Chrysler": 8400,
    "Volvo": 8700,
    "Audi": 8800,
    "Lincoln": 10300,
    "Saturn": 11000,
    "Cadillac": 11000,
    "Mercedes-Benz": 11000,
    "Pontiac": 11300,
    "BMW": 13300
}

maintenance_costs = {key.lower(): value for key, value in maintenance_costs.items()}