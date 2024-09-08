for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            if (not x2 and x1 or not x3 and x1 or x2 and x3) and (not(x1 and not x3) or not x3 and x2):
                print(x1, x2, x3)