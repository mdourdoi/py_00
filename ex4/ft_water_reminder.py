def ft_water_reminder():
    water = int(input("Days since last watering: "))
    if (water >= 4):
        print("Water the plants!")
    else:
        print("Plants are fine")
