import math


class Paint:
    def __init__(self, brand, pricing_options):
        self.brand = brand
        self.pricing_options = pricing_options


class Obstruction:
    def __init__(self, shape, dimensions):
        self.shape = shape
        self.dimensions = dimensions


def calculate_paint_cost(paint_needed, pricing_options):
    min_cost = float('inf')
    min_combination = None

    for combination in pricing_options:
        total_cost = sum(float(price) * math.ceil(paint_needed / bucket_size) for price, bucket_size in combination)

        if total_cost < min_cost:
            min_cost = total_cost
            min_combination = combination

    return min_cost, min_combination


def get_obstruction_details(valid_shapes):
    obstructions = []

    while True:
        num_obstructions = input("Enter the number of obstructions or type 'skip' to continue: ")

        if num_obstructions.lower() == 'skip':
            break

        try:
            num_obstructions = int(num_obstructions)
        except ValueError:
            print("Please enter a valid number or 'skip'.")
            continue

        for i in range(1, num_obstructions + 1):
            shape = input(f"Enter the shape of obstruction {i} ({', '.join(valid_shapes)}): ").lower()

            if shape in valid_shapes:
                dimensions = {}
                for dimension in valid_shapes[shape]:
                    while True:
                        try:
                            dimensions[dimension] = float(input(f"Enter the {dimension} of obstruction {i} in meters: "))
                            break
                        except ValueError:
                            print(f"Invalid input. Please enter a valid number for {dimension}.")
                obstructions.append(Obstruction(shape, dimensions))
                print(f"You have {num_obstructions} obstruction(s).")
            else:
                print(f"Invalid shape. Please enter one of: {', '.join(valid_shapes)}.")

    return obstructions


def calculate_obstruction_size(ob):
    if ob.shape == 'square':
        return ob.dimensions['side'] * ob.dimensions['side']
    elif ob.shape == 'rectangle':
        return ob.dimensions['width'] * ob.dimensions['height']
    elif ob.shape == 'triangle':
        return 0.5 * ob.dimensions['base'] * ob.dimensions['height']
    elif ob.shape == 'semi_circle':
        return 0.5 * 3.1415 * ob.dimensions['radius'] * ob.dimensions['radius']
    elif ob.shape == 'circle':
        return 3.1415 * ob.dimensions['radius'] * ob.dimensions['radius']
    elif ob.shape == 'crescent_moon':
        outer_area = 3.1415 * ob.dimensions['outer_radius'] * ob.dimensions['outer_radius']
        inner_area = 3.1415 * ob.dimensions['inner_radius'] * ob.dimensions['inner_radius']
        return outer_area - inner_area
    elif ob.shape == 'pentagon':
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * ob.dimensions['side'] ** 2
    elif ob.shape == 'hexagon':
        return 1.5 * math.sqrt(3) * ob.dimensions['side'] ** 2
    elif ob.shape == 'parallelogram':
        return ob.dimensions['base'] * ob.dimensions['height']
    elif ob.shape == 'trapezoid':
        return 0.5 * (ob.dimensions['base1'] + ob.dimensions['base2']) * ob.dimensions['height']
    elif ob.shape == 'rhombus':
        return ob.dimensions['side'] ** 2 * math.sin(math.radians(ob.dimensions['angle']))
    else:
        raise ValueError(f"Unsupported shape: {ob.shape}")


def main():
    # Get obstruction details with valid shapes
    valid_shapes = {
        'square': ['side'],
        'rectangle': ['width', 'height'],
        'triangle': ['base', 'height'],
        'semi_circle': ['radius'],
        'circle': ['radius'],
        'crescent_moon': ['outer_radius', 'inner_radius'],
        'pentagon': ['side'],
        'hexagon': ['side'],
        'parallelogram': ['base', 'height'],
        'trapezoid': ['base1', 'base2', 'height'],
        'rhombus': ['side', 'angle'],
    }

    # Get wall dimensions
    height = float(input("Enter the height of the walls in meters: "))
    width = float(input("Enter the width of the walls in meters: "))

    # Calculate wall size in square meters
    wall_size = height * width

    coats = int(input("Enter the number of coats you want to apply to your wall: "))

    # Get obstruction details
    obstruction_list = get_obstruction_details(valid_shapes)

    total_obstruction_size = sum(calculate_obstruction_size(ob) for ob in obstruction_list)

    # Calculate paint needed considering obstructions
    paint_needed = ((wall_size - total_obstruction_size) / 6) * coats

    print(
        f"With {len(obstruction_list)} obstruction(s) totaling {total_obstruction_size:.2f} square meters, you will need {paint_needed:.2f} litres of paint to paint walls with a total area of {wall_size:.2f} square meters."
    )

    # Define paint brands with their respective prices and bucket sizes
    delux_paint = Paint('Delux', [[('22', 2.5)], [('40', 5.0)]])
    layland_paint = Paint('Layland', [[('18', 2.5)], [('33', 5.0)]])
    goodhome_paint = Paint('Goodhome', [[('10', 2.5)], [('16', 5.0)]])

    brands = [delux_paint, layland_paint, goodhome_paint]

    # Brand selection
    print("Available brands:")
    for i, paint in enumerate(brands, start=1):
        print(f"{i}. {paint.brand}")

    selected_brand_index = int(input("Choose a paint brand number from the list: ")) - 1

    if 0 <= selected_brand_index < len(brands):
        selected_paint = brands[selected_brand_index]
        min_cost, min_combination = calculate_paint_cost(paint_needed, selected_paint.pricing_options)

        print(f"The cheapest combination for {paint_needed} litres of {selected_paint.brand} paint is:")
        for price, bucket_size in min_combination:
            buckets_needed = math.ceil(paint_needed / bucket_size)
            print(f"   {buckets_needed} buckets of {bucket_size} litres at £{price} per litre")

        print(f"The total cost is £{min_cost:.2f}.")
    else:
        print("Invalid brand selection.")


if __name__ == "__main__":
    main()




"""
Those obstructions can be different shapes and sizes
Do it wall by wall and save the results
What size are the walls
How much will the paint cost
Offer a selection of brands dependant on the customers requirements
Less than a litre just / by 1000 for 1 ml
i made an extra note to make sure git is working again
change the paint_needed method to change based on the type of paint being used cause different coats are thicker
amount of buckets  it tell you to buy doesnt round down
"""