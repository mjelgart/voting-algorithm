newSeats = 15
totalSeats = 435.0 + newSeats

def algorithm(results):
    global newSeats, totalSeats

    houseSeatsLeft = newSeats
    newSeats = {}
    for party in results.keys():
        newSeats[party] = 0


    while houseSeatsLeft > 0:
        maxDifference = -1.0
        underrepresentedParty = ""
        print("Seat "+ str(51-houseSeatsLeft))
        for party in results.keys():
            difference = results[party][1] - ((results[party][0]+newSeats[party]) / totalSeats)
            print("%s Party difference is %.4f" % (party,difference))
            if difference > maxDifference:
                maxDifference = difference
                underrepresentedParty = party

        print(underrepresentedParty + " Party gets the seat.")
        newSeats[underrepresentedParty] += 1
        houseSeatsLeft -= 1

    for party in results.keys():
        print("%s Party seats were %d, are now %d" % (party, results[party][0], results[party][0]+newSeats[party]))

# key = party name, value = list of [current house seats,presidential popular vote]
electionResults = {
    "Republican":[241,0.4609],
    "Democratic":[194,0.4818],
    "Libertarian":[0,0.0327],
    "Green":[0,0.0106],
    "McMullin":[0,0.0053]
}





if __name__ == "__main__":
    algorithm(electionResults)
