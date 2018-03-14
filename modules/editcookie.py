def editcookie(l, name, cnumber, aors):
    x = int(cnumber)
    if aors == False:
        while x > 0:
            l.remove(str(name.lower()))
            x -= 1
    else:
        while x > 0:
            l.append(str(name.lower()))
            x -= 1