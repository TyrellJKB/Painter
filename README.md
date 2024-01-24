# Paint Estimation Tool

## Overview

The Paint Estimation Tool is a Python program designed to assist users in estimating the amount of paint needed for their walls, taking into account various obstructions. The tool allows users to input wall dimensions, choose the number of coats, specify obstructions, and select a paint brand. The program then calculates the total paint needed, considering obstructions, and recommends the most cost-effective combination of paint buckets.

## Features

1. **Obstruction Handling:**
    - Supports various obstruction shapes, including square, rectangle, triangle, semi-circle, circle, crescent moon, pentagon, hexagon, parallelogram, trapezoid, and rhombus.
    - Users can input the number of each obstruction shape, its dimensions, and the tool calculates the total obstruction size.

2. **Wall Dimensions:**
    - Users input the height and width of the walls in meters.
    - The tool calculates the total wall size in square meters.

3. **Coats and Paint Calculation:**
    - Users specify the number of coats they want to apply to the walls.
    - The program calculates the total amount of paint needed, considering obstructions and coats.

4. **Paint Brand Selection:**
    - The tool offers a selection of paint brands, each with its own pricing options (price per liter and bucket size).
    - Users choose a paint brand, and the program calculates the most cost-effective combination of paint buckets.

5. **User-Friendly Interface:**
    - The tool guides users through the input process, providing clear instructions and validating user inputs.

## Functionality

### Wall Size Calculation

The total wall size is calculated using the formula:
\[ \text{Wall Size} = \text{Height} \times \text{Width} \]

### Obstruction Size Calculation

The size of each obstruction is calculated based on its shape:
- Square: \( \text{Side} \times \text{Side} \)
- Rectangle: \( \text{Width} \times \text{Height} \)
- Triangle: \( 0.5 \times \text{Base} \times \text{Height} \)
- Semi-circle: \( 0.5 \times \pi \times \text{Radius} \times \text{Radius} \)
- Circle: \( \pi \times \text{Radius} \times \text{Radius} \)
- Crescent Moon: \( \text{Outer Area} - \text{Inner Area} \) (based on radius values)
- Pentagon: \( 0.25 \times \sqrt{5 \times (5 + 2 \times \sqrt{5})} \times \text{Side}^2 \)
- Hexagon: \( 1.5 \times \sqrt{3} \times \text{Side}^2 \)
- Parallelogram: \( \text{Base} \times \text{Height} \)
- Trapezoid: \( 0.5 \times (\text{Base1} + \text{Base2}) \times \text{Height} \)
- Rhombus: \( \text{Side}^2 \times \sin(\text{Angle}) \)

### Paint Needed Calculation

The total amount of paint needed is calculated using the formula:
\[ \text{Paint Needed} = \left( \frac{\text{Wall Size} - \text{Total Obstruction Size}}{6} \right) \times \text{Number of Coats} \]

### Paint Brand Selection

The program recommends the most cost-effective combination of paint buckets from the selected brand. The calculation involves iterating through pricing options to find the minimum cost.

## Dependencies

This program requires Python 3.

## Future Improvements

1. **Wall-by-Wall Estimation:**
    - Enhance the tool to estimate paint requirements for each wall separately and save the results.

2. **Dynamic Paint Thickness:**
    - Modify the `paint_needed` method to adjust the amount of paint needed based on the type of paint being used, considering different thickness levels.

3. **Brand Selection Enhancement:**
    - Improve the brand selection process, allowing users to specify preferences and requirements for the paint brand.

4. **Decimal Liter Conversion:**
    - For amounts less than a liter, automatically convert to milliliters (divide by 1000).

5. **Buckets Needed Rounding:**
    - Address the issue where the number of buckets needed is not rounded down.
