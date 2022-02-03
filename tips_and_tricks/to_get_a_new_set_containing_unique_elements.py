"""
You can use .intersection() to get a new set containing unique elements that are present inside set1 and set2

https://twitter.com/testdrivenio/status/1488561537711153153
"""


def return_intersection(winners, players):
    new_intersection = winners.intersection(players)
    print(new_intersection)
    return new_intersection


winners = {"John", "Lulu"}
players = {"Pedro", "John", "Daren", "Lulu", "Sizla"}

return_intersection(winners, players)
