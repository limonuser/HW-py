def r_3max(tp:tuple)-> tuple:
    tp = list(tp)
    tp.sort(reverse = True)
    while len(tp) > 3:
        tp.pop()
    return tp
if __name__ == "__main__":
    ls = [(), (1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
    for t in ls:
        print(r_3max(t))