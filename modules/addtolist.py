def savetolist(l, x):
    if len(l) <= 19:
        l.append(int(x))
    else:
        del l[0]
        l.append(int(x))