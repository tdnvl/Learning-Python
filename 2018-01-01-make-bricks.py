def make_bricks(small, big, goal):
    a = goal / 5
    # if a >= 1 we can use at least one big brick
    # if a < 1 we cannot use a big brick
    b = goal % 5
    # if b == 0 the goal is a multiple of 5
    # if b != 0 we need to check if we have enough small bricks
    # to reach the goal
    c = int(a)
    d = c*big + b*small

    if b == 0:
        if big >= a:
            return True
        elif big < a and ((a - big) * 5) <= small:
            return True
        elif big < a and (a - big)*5 > small:
            return False
        elif goal > small:
            return False
        elif goal <= small:
            return True
    elif b != 0:
      if big < a and small >= b:
        return True
      elif big < a and small < b:
        return False
    elif small == 0 and b == 0 and big >= a:
      return True
    elif small == 0 and b == 0 and big < a:
      return False
