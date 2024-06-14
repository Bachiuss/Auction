import logo
import os

clear = lambda: os.system('cls')
print(logo.logo)

bids = {}


def highest_price(bidding_record):
    score = 0
    for i in bidding_record:
        amount = bidding_record[i]
        if amount > score:
            score = amount
            winner = i
    print(f"The winner is {winner} with a bid of ${score}")


continue_auction = True
while continue_auction:
    name = input("What is ur name?: ")
    price = int(input("What is ur Bid?: $"))
    bids[name] = price
    other_user = input("Is there anyone who wants to bid? 'y' or 'n':\n").lower()
    if other_user == "n":
        continue_auction = False
        highest_price(bids)
    elif other_user == "y":
        os.clear()
