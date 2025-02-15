import numpy as np
import pandas as pd


def least_squares_regression(years, demand):
    """Performs Least Squares Regression (KMNK) to predict demand."""
    X = np.vstack([np.ones(len(years)), years]).T
    coeffs = np.linalg.inv(X.T @ X) @ X.T @ demand
    return coeffs


def predict_demand(coeffs, year):
    """Predicts transport demand for a given year using regression coefficients."""
    return np.array([1, year]) @ coeffs


def optimize_fleet(demand, vehicles):
    """Allocates the fleet to maximize profit."""
    allocation = {v: 0 for v in vehicles}
    remaining_demand = demand

    # Assign large buses first for efficiency
    for vehicle, data in sorted(vehicles.items(), key=lambda x: -x[1]["capacity"]):
        num_vehicles = int(remaining_demand // data["capacity"])
        remaining_demand -= num_vehicles * data["capacity"]
        allocation[vehicle] = num_vehicles

    # If there's leftover demand, add a small bus
    if remaining_demand > 0:
        allocation["Small Bus"] += 1

    # Calculate total cost, revenue, and profit
    total_cost = sum(allocation[v] * vehicles[v]["cost"] for v in allocation)
    total_revenue = sum(
        allocation[v] * vehicles[v]["capacity"] * vehicles[v]["revenue_per_passenger"]
        for v in allocation
    )
    total_profit = total_revenue - total_cost

    return allocation, total_profit


# Historical data
years = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
demand_city_a = np.array([12, 9, 10, 19, 13, 8, 12, 14, 11, 10])
demand_city_b = np.array([14, 11, 12, 16, 18, 10, 13, 17, 15, 12])

# Compute regression coefficients
coeffs_a = least_squares_regression(years, demand_city_a)
coeffs_b = least_squares_regression(years, demand_city_b)

# Predict 2024 demand
year_2024 = 2024
demand_a = predict_demand(coeffs_a, year_2024)
demand_b = predict_demand(coeffs_b, year_2024)

# Fleet data
vehicles = {
    "Small Bus": {"capacity": 5, "cost": 50, "revenue_per_passenger": 15},
    "Medium Bus": {"capacity": 10, "cost": 80, "revenue_per_passenger": 15},
    "Large Bus": {"capacity": 20, "cost": 120, "revenue_per_passenger": 15},
}

# Optimize fleet usage
allocation_a, profit_a = optimize_fleet(demand_a, vehicles)
allocation_b, profit_b = optimize_fleet(demand_b, vehicles)

# Display results
results = pd.DataFrame(
    {
        "City": ["City A", "City B"],
        "Predicted Demand": [demand_a, demand_b],
        "Small Buses": [allocation_a["Small Bus"], allocation_b["Small Bus"]],
        "Medium Buses": [allocation_a["Medium Bus"], allocation_b["Medium Bus"]],
        "Large Buses": [allocation_a["Large Bus"], allocation_b["Large Bus"]],
        "Total Profit (€)": [profit_a, profit_b],
    }
)

print(results)
