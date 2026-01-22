def ft_harvest_total():
    res = 0
    for i in (1, 2, 3):
        res += int(input(f"Day {i} harvest: "))
    print(f"Total harverst: {res}")
