import random


class Tile(object):

    tile_numbers = range(0, 10)
    names = ["Mediterranean Ave", "Community Chest", "Baltic Ave", "Income Tax", "Reading Railroad",
             "Oriental Ave", "Chance", "Vermont Ave", "Connecticut Ave", "Jail"]

    def __init__(self, name, tile_number, landed_on):
        self.name = name
        self.tile_number = tile_number
        self.landed_on = landed_on


class Property(Tile):

    def __init__(self, name, tile_number, landed_on, price, owned_by, mortgaged, color):
        Tile.name = name
        Tile.tile_number = tile_number
        Tile.landed_on = landed_on
        self.price = price
        self.owned_by = owned_by
        self.mortgaged = mortgaged
        self.color = color
        super(Property, self).__init__(name, tile_number, landed_on)


class Directive(Tile):

    directive_type = ["draw card", "pay", "jail", "collect"]

    def __init__(self, name, tile_number, landed_on, directive_type):
        Tile.name = name
        Tile.tile_number = tile_number
        Tile.landed_on = landed_on
        self.directive_type = directive_type
        super(Directive, self).__init__(name, tile_number, landed_on)


mediterranean_ave = Property("Mediterranean Ave", 0, False, 60, None, False, "Brown")
community_chest = Directive("Community Chest", 1, False, "draw card")
baltic_ave = Property("Baltic Ave", 2, False, 80, None, False, "Brown")
income_tax = Directive("Income Tax", 3, False, "pay")
reading_railroad = Property("Reading Railroad", 4, False, 200, None, False, "Black")
oriental_ave = Property("Oriental Ave", 5, False, 90, None, False, "Light Blue")
chance = Directive("Chance", 6, False, "draw card")
vermont_ave = Property("Vermont Ave", 7, False, 90, None, False, "Light Blue")
connecticut_ave = Property("Connecticut Ave", 8, False, 110, None, False, "Light Blue")
jail = Directive("Jail", 9, False, "visiting")
go = Directive("Go", 10, False, "collect")

real_estate_list = [mediterranean_ave, community_chest, baltic_ave, income_tax, reading_railroad,
                    oriental_ave, chance, vermont_ave, connecticut_ave, jail, go]