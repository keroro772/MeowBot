from modules import indexinsubstring , numbcheck
def bet(message, bopen, sender, betters, bets):
    if len(message) != 4:
        if bopen == True:
            if numbcheck.is_num(message[4]) == True:
                if int(message[4]) <= 160:
                    if sender in betters:
                        return('You have already made a bet wait until next round')
                    else:
                        if message[4] in bets:
                            return('That number has already been taken please try another.')
                        else:
                            bets.append(message[4])
                            betters.append(sender)
                            return(sender + ' Your bet has been saved good luck')
                else:
                    return('Your bet was too large it can\'t be any bigger than 160')
            else:
                return('Please use a number next time, baka!')
        else:
            return('Bets are not open.')
    else:
        return('Please specify a number next time')
    
def changebet(message, bopen, sender, betters, bets):
    if len(message) != 4:
        if bopen == True:
            if numbcheck.is_num(message[4]) == True:
                if int(message[4]) <= 160:
                    if sender in betters:
                        if message[4] in bets:
                            return('That number has already been taken please try another.')
                        else:
                            bets[indexinsubstring.index_containing_substring(betters, sender)] = message[4]
                            return(sender + ' your bet has been changed to: ' + message[4])
                    else:
                        return( 'Please make a bet using !bet before you try to change it')
                else:
                    return('Your bet was too large it can\'t be any bigger than 160')
            else:
                return('Please use a number next time, baka!')
        else:
            return('Bets are not open.')
    else:
        return('Please specify a number next time')        