def list_generator():
    import random
    random.seed(None,2)
    non_deduped_list = []
    # I'm liminting the length of the list to 30 elements, so it's more readable.
    list_length = random.randint(1,30)
    for i in range(list_length):
        new_integer = random.randint(1,99)
        non_deduped_list.append(new_integer)
    return non_deduped_list

def deduping_list(long_list):
    # set(long_list)
    # return list(long_list)
    print(sorted(list(set(long_list))))


a = list_generator()
print(a)
print(sorted(a))
# c = [1,1,2,2,3,3]
# b = set(c)
# print(list(b))
deduping_list(a)



# origin = [1,1,3,5,7,8,12,4,12,1,7]
# deduped = set(origin)
# print(list(deduped))
