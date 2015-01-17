def start_game():
    print """Welcome to Python-powered Monopoly!


    """
    number_of_players()


def number_of_players():
    print """How many players will there be?
    Pick a number 2 - 4 and press Enter.

    """
    num_players = raw_input(">>>")
    numbers = ["2", "3", "4"]
    if num_players in numbers:
        print "We'll get a game set up for " + str(num_players) + """ players.


        """
        choose_tokens(num_players)
        return num_players
    else:
        number_of_players()


tokens = ["dog", "car", "iron", "thimble"]


def choose_tokens(num_players):
    print "Player One, please choose a token from this list: " + str(tokens)
    choice1 = raw_input(">>>")
    if choice1 in tokens:
        index1 = tokens.index(choice1)
        tokens.pop(index1)
        choose_tokens2(choice1, num_players)
        return choice1
    else:
        print "You didn't enter an eligible token..."
        choose_tokens(num_players)


def choose_tokens2(choice1, num_players):
    print "Player One chose " + str(choice1) + ".  Player Two, please choose a token: " + str(tokens)
    choice2 = raw_input(">>>")
    if choice2 in tokens:
        index2 = tokens.index(choice2)
        tokens.pop(index2)
        if int(num_players) > 2:
            choose_tokens3(choice2, num_players)
            return choice2
        else:
            print "Player Two chose " + str(choice2)
    else:
        print "That's not an option..."
        choose_tokens2(choice1, num_players)


def choose_tokens3(choice2, num_players):
    print "Player Two chose " + str(choice2) + ".  Player Three, which do you want? " + str(tokens)
    choice3 = raw_input(">>>")
    if choice3 in tokens:
        index3 = tokens.index(choice3)
        tokens.pop(index3)
        if int(num_players) > 3:
            choose_tokens4(choice3)
            return choice3
        else:
            print "Player Three chose " + str(choice3)
    else:
        print "Sorry..."
        choose_tokens3(choice2, num_players)


def choose_tokens4(choice3):
    print "Player Three chose " + str(choice3) + ".  Player Four, you get the " + str(tokens) + " token."

