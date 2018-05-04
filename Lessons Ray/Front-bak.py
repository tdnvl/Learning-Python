def front_back(str):
    l_str = []
    for i in str:
        l_str.append(i)
    l = len(l_str)
    if l == 1:
        print(str)
    else:
        last = l_str.pop()
        first = l_str.pop(0)
        middle = l_str[0:(l-2)]
        middle = ''.join(middle)
        new_str = last + middle + first
        print(new_str)

front_back('code')
front_back('a')
front_back('ab')
