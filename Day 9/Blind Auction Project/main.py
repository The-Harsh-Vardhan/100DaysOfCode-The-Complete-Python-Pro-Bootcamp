import art
print(art.logo)

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    maximum_bid = 0
    auction_winner = ""
    for key in bidders:
        if bidders[key] > maximum_bid:
            maximum_bid = bidders[key]
            auction_winner = key
    print(f"The Winner of the Auction is {auction_winner} with a bid of Rs {maximum_bid}")

bidders = {}
auction_completed = False

while not auction_completed:
    # TODO-1: Ask the user for input
    bidder_name = input("What is your Name? : ")
    bidding_value = int(input("What is your Bid? : Rs "))

    # TODO-2: Save data into dictionary {name: price}
    bidders[bidder_name] = bidding_value

    # TODO-3: Whether if new bids need to be added
    bidders_left = input("Are they any other bidders left? 'yes' or 'no' \n").lower()
    print("\n" * 20)
    if bidders_left == "no":
        auction_completed = True
        find_highest_bidder(bidders)

