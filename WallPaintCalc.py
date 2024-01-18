brands = ['delux', 'Layland', 'Goodhome',]
litres_of_paint = 0
price = 0




wall_size = int(input("Enter the amount size of your wall in meters squared "))
coats = int(input("Enter the amount of coats you want to apply to your wall"))
obstructions = int(input("Enter the square meters of obstructions such as Windows or Sockets"))


paint_needed = ((wall_size-obstructions) / 6)*coats

print(f"You will need {paint_needed}, litres of paint to paint a wall that is {wall_size}, meters")


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

