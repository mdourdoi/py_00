def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if (unit == "packets"):
        print(seed_type.capitalize(), f"seeds: {quantity}", "available")
    elif (unit == "grams"):
        print(seed_type.capitalize(), f"seeds: {quantity}", "total")
    elif (unit == "area"):
        print(seed_type.capitalize(), f"covers {quantity}", "square meters")
    else:
        print("Unknown unit type")
