def ft_count_harvest_recursive(days=-1, final=1):
    if (days == -1):
        days = int(input("Days until harvest: "))
    if (days == 0):
        if (final):
            print("Harvest time")
        return
    ft_count_harvest_recursive(days-1, 0)
    print(f"Day {days}")
    if (final):
        print("Harvest time")
