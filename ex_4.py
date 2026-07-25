def find_genre(ls:list, genre:str)-> list:
    res = []
    for x in ls:
        if x["genre"] == genre:
            res.append(x)
    return res

if __name__ == "__main__":
    ls = [
        {"title": "Movie 1", "genre": "Action", "price": 10.99},
        {"title": "Movie 2", "genre": "Comedy", "price": 9.99},
        {"title": "Movie 3", "genre": "Action", "price": 12.99},
        {"title": "Movie 4", "genre": "Comedy", "price": 11.99},
        {"title": "Movie 5", "genre": "Detective", "price": 14.99},
    ]
    print(find_genre(ls, "Action"))
    print(find_genre(ls, "Comedy"))
    print(find_genre(ls, "Detective"))