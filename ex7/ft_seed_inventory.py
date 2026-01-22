def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    seed = seed_type.capitalize()
    if (unit == "packets"):
        print(seed, f"seeds: {quantity}", "available")
    elif (unit == "grams"):
        print(seed, f"seeds: {quantity}", "total")
    elif (unit == "area"):
        print(seed, f"seeds: covers {quantity}", "square meters")
    else:
        print("Unknown unit type")
