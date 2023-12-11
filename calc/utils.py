def calculate_weight_and_price(height, length, rolls, diameter, cell_size, cost_per_kg):
    # Convert Decimal values to float
    height = float(height)
    length = float(length)
    rolls = float(rolls)
    diameter = float(diameter)
    cell_size = float(cell_size)

    weight_per_square_meter = 13.4 * diameter**2 / cell_size
    weight = height * length * rolls * weight_per_square_meter / 1000000
    total_price = weight * cost_per_kg
    weight = round(weight, 2)
    total_price = round(total_price, 2)

    return weight, total_price
