from config import app_properties

locations, trucks = [], []
map_size = 5 if app_properties.PROBLEM == 1 else 60
truck_size = 5 if app_properties.PROBLEM == 1 else 10
bike_map = [[0] * map_size for _ in range(map_size)]
problem = app_properties.PROBLEM


def print_bike_map():
    for row in bike_map:
        print(*row)


def position(location_id):
    return (map_size - 1) - (location_id % map_size), location_id // map_size


def refresh_info(kakao):
    global locations, trucks

    locations = kakao.locations()
    trucks = kakao.trucks()

    for location in locations:
        x, y = position(location.id)
        bike_map[x][y] = location.located_bikes_count


def move_truck(truck, x, y):
    truck_x, truck_y = position(truck.location_id)

    for _ in range(abs(truck_x - x)):
        if truck_x - x > 0:
            truck.up()
        else:
            truck.down()

    for _ in range(abs(truck_y - y)):
        if truck_y - y > 0:
            truck.left()
        else:
            truck.right()


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
