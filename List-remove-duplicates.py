def list_generator():
    import random
    random.seed(None,2)
    non_deduped_list = []
    list_length = random.randint(1,99)
    print(list_length)
    for i in range(list_length):
        new_integer = random.randint(1,99)
        non_deduped_list.append(new_integer)
    print(non_deduped_list)

list_generator()






# origin = [1,1,3,5,7,8,12,4,12,1,7]
# deduped = set(origin)
# print(list(deduped))
