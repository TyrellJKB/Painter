class Paint:
    def __init__(self, brand, price_per_liter, bucket_size):
        self.brand = brand
        self.price_per_liter = price_per_liter
        self.bucket_size = bucket_size

def calculate_paint_cost(wall_size, coats, obstructions, paint_needed, paint):
    buckets_needed = paint_needed / paint.bucket_size
    total_cost = buckets_needed * paint.price_per_liter
    return total_cost

# Define paint brands with their respective prices and bucket sizes
delux_paint = Paint('Delux', 8.80, 2.5)
layland_paint = Paint('Layland', 2.20, 2.5)
goodhome_paint = Paint('Goodhome', 6.40, 2.5)

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
for paint in brands:
    print(paint.brand)

selected_brand = input("Choose a paint brand from the list: ")

# Find the selected brand object
selected_paint = next((paint for paint in brands if paint.brand.lower() == selected_brand.lower()), None)

if selected_paint:
    total_cost = calculate_paint_cost(wall_size, coats, obstructions, paint_needed, selected_paint)
    print(f"The total cost for {paint_needed} litres of {selected_paint.brand} paint is £{total_cost:.2f}.")
else:
    print("Invalid brand selection.")

"""
Tape measurements only
THere can be obstructions
Those obstructions can be different shapes and sizes
Do it wall by wall and save the results
What size are the walls
How much will the paint cost
Offer a selection of brands dependant on the customers requirements
Less than a litre just / by 1000 for 1 ml
i made an extra note to make sure git is working again
"""

