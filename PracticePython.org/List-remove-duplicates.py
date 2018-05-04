def list_generator(): # Builds a list of 1-30 elements in range 1-99.
    import random
    random.seed(None,2)
    non_deduped_list = []
    # I'm arbitrarily limiting the length of the list to 30 elements.
    list_length = random.randint(1,30)
    for i in range(list_length):
        # I'm arbitrarily limiting the range to 1-99.
        new_integer = random.randint(1,99)
        non_deduped_list.append(new_integer)
    return non_deduped_list

def deduping_list(long_list):
    # This looks efficient, but not very good practice. I need to ask.
    print(sorted(list(set(long_list))))


a = list_generator()
print(a)
print(sorted(a))
deduping_list(a)
