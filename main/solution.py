import common


def do_nothing(kakao):
    for _ in range(720):
        commands = [{'truck_id': i, 'command': [0]} for i in range(common.truck_size)]
        print(kakao.simulate(commands))


def solution(kakao):
    for _ in range(720):
        common.refresh_info(kakao)
        # common.print_bike_map()
        bike_map, locations, trucks = common.bike_map, common.locations, common.trucks

        for _ in range(common.truck_size):
            min_location = min(locations, key=lambda location: location.located_bikes_count)
            max_location = max(locations, key=lambda location: location.located_bikes_count)

            min_x, min_y = common.position(min_location.id)
            max_x, max_y = common.position(max_location.id)

            truck_selected = find_closest_truck(trucks, min_x, min_y, 'down')
            common.move_truck(truck_selected, min_x, min_y)
            truck_selected.down_bike()
            bike_map[min_x][min_y] += 1

            while bike_map[min_x][min_y] < 4 and truck_selected.loaded_bikes_count > 0 and len(truck_selected.command) < 10:
                truck_selected.down_bike()
                bike_map[min_x][min_y] += 1

            if bike_map[max_x][max_y] > 2:
                truck_selected = find_closest_truck(trucks, max_x, max_y, 'load')
                common.move_truck(truck_selected, max_x, max_y)
                truck_selected.load_bike()
                bike_map[max_x][max_y] -= 1

                while bike_map[max_x][max_y] > 5 and truck_selected.loaded_bikes_count < 20 and len(truck_selected.command) < 10:
                    truck_selected.load_bike()
                    bike_map[max_x][max_y] -= 1

        print(kakao.simulate([t.get_command() for t in trucks]))


# flag: 'load' 자전거 실으러 가는중, 'down' 자전거 내리러 가는중
def find_closest_truck(trucks, x, y, flag):
    truck_selected, min_distance = trucks[0], 1000

    for truck in trucks:
        if flag == 'down' and truck.loaded_bikes_count < 1:
            continue
        elif flag == 'load' and truck.loaded_bikes_count >= 20:
            continue

        truck_x, truck_y = common.position(truck.location_id)
        distance = common.distance(truck_x, truck_y, x, y)

        if distance < min_distance and len(truck.command) + distance + 1 <= 10:
            truck_selected, min_distance = truck, distance

    return truck_selected
