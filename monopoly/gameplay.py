def start_game():
    print """Welcome to Python-powered Monopoly!


    """
    number_of_players()


def number_of_players():
    print """How many players will there be?
    Pick a number 2 - 4 and press Enter.

    """
    players = raw_input(">>>")
    numbers = ["2", "3", "4"]
    if players in numbers:
        print "We'll get a game set up for " + str(players) + """ players.


        """
        choose_tokens(number)
        return players
    else:
        number_of_players()

number = number_of_players()

tokens = ["dog", "car", "iron", "thimble"]


def choose_tokens(number):
    print "Player One, please choose a token from this list " + str(tokens)
    choice1 = raw_input(">>>")
    if choice1 in tokens:
        index1 = tokens.index(choice1)

        choose_tokens2(index1, number)
        return index1
    else:
        print "You didn't enter an eligible token..."
        choose_tokens(number)


def choose_tokens2(index1, number):
    print "Player One chose " + str(tokens.pop(index1)) + ".  Player Two, please choose a token: " + str(tokens)
    choice2 = raw_input(">>>")
    if choice2 in tokens:
        index2 = tokens.index(choice2)
        if number > 2:
            choose_tokens3(index2, number)
            return index2
    else:
        print "That's not an option..."
        choose_tokens2(index1, number)


def choose_tokens3(index2, number):
    print "Player Two chose " + str(tokens.pop(index2)) + ".  Player Three, which do you want? " + str(tokens)
    choice3 = raw_input(">>>")
    if choice3 in tokens:
        index3 = tokens.index(choice3)
        if number > 3:
            choose_tokens4(index3)
            return index3
    else:
        print "Sorry..."
        choose_tokens3(index2, number)


def choose_tokens4(index3):
    print "Player Three chose " + str(tokens.pop(index3)) + ".  Player Four, you get the " + str(tokens) + " token."

