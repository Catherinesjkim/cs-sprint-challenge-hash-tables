"""
`source` string = starting airport
`destination` string = next airport along my trip. 

The ticket for my first flight has a destination with a `source` of `NONE`

The ticket for my final flight has a `source` with a `destination` of `NONE`. 
"""
#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        
    def get_source(self):
        return self.source
    
    def get_destination(self):
        return self.destination

def hash_tickets(tickets, length):
    dict = {}
    for i in range(length):
        ticket = tickets[i]
        source, destination = ticket.get_source(), ticket.get_destination()
        dict[source] = destination
    return dict
    
def reconstruct_trip(tickets, length):
    routes = hash_tickets(tickets, length)
    dict  = [routes["NONE"]] * length
    
    for i in range(1, len(dict)):
        dict[i] = routes[dict[i -1]]
        
    return dict


# Driver code
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "CID")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("CID", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

#  expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD", "NONE"]

print(reconstruct_trip(tickets, 10))
