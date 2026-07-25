def func1(st:str) -> str:
    alphas = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    if st in "aeuio":
        return st
    else:
        res = 0
        for x in alphas:
            if st == alphas[x]:
                res = x
        if res <= 3:   
            return alphas[1]
        elif res > 3 and res <= 7:
            return alphas[5]
        elif res > 7 and res <= 12:
            return alphas[9]
        elif res > 12 and res <= 18:
            return alphas[15]
        elif res > 18:
            return alphas[21]
if __name__ == "__main__":
    print(func1("h"))
    