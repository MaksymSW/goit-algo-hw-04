def get_cats_info(path):
    try:
        with open(path, mode='r', encoding='UTF-8') as cat:
            cat_list = []
            # cats = [el.strip() for el in cat.readlines()]
            # print(cats)
            for el in cat:
                    cats = el.strip().split(',')
                    print(cats)
                    cat_list.append({"id": cats[0], "name": cats[1], "age": cats[2]})     
    except Exception:
        return FileNotFoundError
    return cat_list

cats_info = get_cats_info(r"d:\Обучение\GoIT\Python\HomeWork\goit-algo-hw-04\cats_file.txt")
print(cats_info)

