def color_time(ls:list)-> int:
    n = 0
    res = []
    for x in range(len(ls)):
        if x == len(ls) - 1:
            n += 2
            break
        if ls[x] == ls[x+1]:
            n += 2
        else:
            n += 3
    return n
if __name__ == "__main__":
    p = ["Red", "Green", "Blue"]
    p2 = ["Red", "Red", "Red"]
    p3 = ["Red", "Green", "Red", "Green"]
    p4 = ["Green"]
    print(color_time(p))
    print(color_time(p2))
    print(color_time(p3))
    print(color_time(p4))