def getrank(cookies):
    rank = ''
    x = cookies
    if x >= 10000:
        rank = ' Is a Cat God'
    elif x >= 5000:
        rank = ' Is a Mythical Cat'
    elif x >= 1500:
        rank = ' Is a Magical Cat'
    elif x >= 500:
        rank = ' Is an Alpha Cat'
    elif x >= 150:
        rank = ' Is a Beta Cat'
    elif x >= 50:
        rank = ' Is a Kappa Cat'
    elif x >= 15:
        rank = ' Is a Cute Kitten'
    elif x == 5:
        rank = ' Is a Little kitten'
    return rank

def getrankpercent(total, user):
    rank = ''
    if total.index(user) > int(total.index(total[int(abs(0.999 * len(total)))])):
        rank = ' Is a Cat God.'
    elif total.index(user) > int(total.index(total[int(abs(0.855 * len(total)))])):
        rank = ' Is a Mythical Cat.' 
    elif total.index(user) > int(total.index(total[int(abs(0.755 * len(total)))])):
        rank = ' Is a Magical Cat.' 
    elif total.index(user) > int(total.index(total[int(abs(0.555 * len(total)))])):
        rank = ' Is an Alpha Cat.'
    elif total.index(user) > int(total.index(total[int(abs(0.255 * len(total)))])):
        rank = ' Is a Beta Cat.'
    elif total.index(user) > int(total.index(total[int(abs(0.155 * len(total)))])):
        rank = ' Is a Keepo Cat.'
    elif total.index(user) > int(total.index(total[int(abs(0.01 * len(total)))])):
        rank = ' Is a Cute Kitten.'
    else:
        rank = ' Is a Little kitten.' 
    return rank