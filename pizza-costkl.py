# Pizza cost calculator
def calculate_pizza_cost():
    print("---Pizza Cost Calculator---")
    # Fixed costs
    labour_cost = 0.75
    rent_cost = 1.00
    material_rate = 0.50
    hst_rate = 0.13

# Get user input for diameter
    diameter = float(input("Enter the diameter of the pizza: "))
# Calculate material cost
    material_cost = material_rate * diameter
# Calculate subtotal
    subtotal = labour_cost + rent_cost + material_cost
# Calculate total with HST
    total = subtotal * (1 + hst_rate)
# Round the total to 2 decimal places
    total = round(total, 2)
# Display the total
    print(f"The total cost is: ${total}")
calculate_pizza_cost()