import random


class Player(object):

    token = ["dog", "car", "iron", "thimble"]

    def __init__(self, token, cash, properties, current_tile, current_roll, in_jail, turn, order):
        self.token = token
        self.cash = cash
        self.properties = properties
        self.current_tile = current_tile
        self.current_roll = current_roll
        self.in_jail = in_jail
        self.turn = turn
        self.order = order

    def move_token(self):
        Player.current_roll = Player.roll_the_dice(self)
        Player.current_tile = Player.current_tile + Player.current_roll
        print Player.current_tile
        return Player.current_tile

    def roll_the_dice(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        result = first + second
        self.current_roll = result
        return result


dog = Player("dog", 1500, None, -1, 0, False, False, 0)
car = Player("car", 1500, None, -1, 0, False, False, 0)
iron = Player("iron", 1500, None, -1, 0, False, False, 0)
thimble = Player("iron", 1500, None, -1, 0, False, False, 0)

token_list = [dog, car, iron, thimble]