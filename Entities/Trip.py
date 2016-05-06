class Trip(object):
    tripID=0
    start=0 # event id
    end=0 # event id
    budget=0
    def __init__(self,tripID,start,end,budget):
        self.tripID=tripID
        self.start=start
        self.end=end
        self.budget=budget