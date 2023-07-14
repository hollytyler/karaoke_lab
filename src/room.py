class Rooms:
    def __init__(self, number):
        self.number = number
        self.guests_in_room = []

    def add_guest_to_room(self, guest):
        self.guests_in_room.append(guest)