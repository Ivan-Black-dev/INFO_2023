for x in range(0, 17):
    n1 = 6 * 17**4 + 6 * 17**3 + x * 17**2 + 6 * 17**1 + 3
    n2 = 5 * 17**4 + x * 17**3 + 8 * 17**2 + 1 * 17**1 + 0
    r = n1 - n2
    if r % 11 == 0:
        print(r/11)
