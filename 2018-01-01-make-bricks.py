def make_bricks(small, big, goal):
    bigg = 5*big
    if bigg != 0:
        remainder = goal % bigg
    # goal made of small bricks only
    if small != 0 and 1 >= goal >= small:
        return True
    elif small != 0 and bigg != 0 and 1 >= remainder >= small:
        return True

