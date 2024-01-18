class Paint:
    def __init__(self, brand, pricing_options):
        self.brand = brand
        self.pricing_options = pricing_options

def calculate_paint_cost(wall_size, coats, obstructions, paint_needed, pricing_options):
    min_cost = float('inf')
    min_combination = None

    for combination in pricing_options:
        total_cost = 0
        for price, bucket_size in combination:
            buckets_needed = paint_needed / bucket_size
            total_cost += buckets_needed * float(price)

        if total_cost < min_cost:
            min_cost = total_cost
            min_combination = combination

    return min_cost, min_combination

# Define paint brands with their respective prices and bucket sizes
delux_paint = Paint('Delux', [[('8.80', 2.5)], [('4.00', 5.0)]])
layland_paint = Paint('Layland', [[('2.20', 2.5)], [('2.20', 5.0)]])
goodhome_paint = Paint('Goodhome', [[('6.40', 2.5)], [('3.20', 5.0)]])

brands = [delux_paint, layland_paint, goodhome_paint]

# Get wall dimensions
height = float(input("Enter the height of the walls in meters: "))
width = float(input("Enter the width of the walls in meters: "))

# Calculate wall size in square meters
wall_size = height * width

coats = int(input("Enter the number of coats you want to apply to your wall: "))
obstructions = int(input("Enter the square meters of obstructions such as windows or sockets: "))

paint_needed = ((wall_size - obstructions) / 6) * coats

print(f"You will need {paint_needed} litres of paint to paint walls with a total area of {wall_size} square meters.")

# Brand selection
print("Available brands:")
for i, paint in enumerate(brands, start=1):
    print(f"{i}. {paint.brand}")

selected_brand_index = int(input("Choose a paint brand number from the list: ")) - 1

if 0 <= selected_brand_index < len(brands):
    selected_paint = brands[selected_brand_index]
    min_cost, min_combination = calculate_paint_cost(wall_size, coats, obstructions, paint_needed, selected_paint.pricing_options)

    print(f"The cheapest combination for {paint_needed} litres of {selected_paint.brand} paint is:")
    for price, bucket_size in min_combination:
        print(f"   {bucket_size} litres at £{price} per litre")

    print(f"The total cost is £{min_cost:.2f}.")
else:
    print("Invalid brand selection.")





"""
Those obstructions can be different shapes and sizes
Do it wall by wall and save the results
What size are the walls
How much will the paint cost
Offer a selection of brands dependant on the customers requirements
Less than a litre just / by 1000 for 1 ml
i made an extra note to make sure git is working again
"""