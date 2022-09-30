
class Location:
    def __init__(self, location):
        self.id = int(location['id'])
        self.located_bikes_count = int(location['located_bikes_count'])


class Truck:
    def __init__(self, truck):
        self.id = int(truck['id'])
        self.location_id = int(truck['location_id'])
        self.loaded_bikes_count = int(truck['loaded_bikes_count'])
        self.command = []

    def load_bike(self):
        self.command.append(5)
        self.loaded_bikes_count += 1

    def down_bike(self):
        self.command.append(6)
        self.loaded_bikes_count -= 1

    def up(self):
        self.command.append(1)
        self.location_id += 1

    def down(self):
        self.command.append(3)
        self.location_id -= 1

    def left(self):
        self.command.append(4)
        self.location_id -= 5

    def right(self):
        self.command.append(2)
        self.location_id += 5

    def get_command(self):
        return {'truck_id': self.id, 'command': self.command if self.command else [0]}
