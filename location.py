class Location:
    def __init__(self, ID, name, userID, latitude, longitude, rating):
        self.ID = ID
        self.name = name
        self.userID = userID
        self.latitude = latitude
        self.longitude = longitude
        self.rating = rating

    def get_coords(self):
        return (self.latitude, self.longitude)