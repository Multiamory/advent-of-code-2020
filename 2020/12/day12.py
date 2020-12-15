DEGREE_VECTORS = {
    0: (1, 0),
    90: (0, -1),
    180: (-1, 0),
    270: (0, 1),
}

DEGREE_ROTATION = {
    0: lambda x: x,
    90: lambda x: tuple([x[1], -x[0]]),
    180: lambda x: tuple([-x[0], -x[1]]),
    270: lambda x: tuple([-x[1], x[0]]),
}

DIRECTIONS = {"R": 1, "L": -1}

COMPASS_DEGREES = {"E": 0, "S": 90, "W": 180, "N": 270}


def waypoint_operation(position, waypoint, operation):
    letter = operation[:1]
    amount = int(operation[1:])
    if letter == "F":
        position = move_to_waypoint(position, waypoint, amount)
    elif letter in ["R", "L"]:
        waypoint = rotate_waypoint(waypoint, letter, amount)
    else:
        waypoint = move_direction(waypoint, letter, amount)

    return position, waypoint


def rotate_waypoint(waypoint, direction, amount):
    degrees = (amount * DIRECTIONS[direction]) % 360
    waypoint = DEGREE_ROTATION[degrees](waypoint)
    return waypoint


def move_to_waypoint(position, waypoint, amount):
    position = tuple(a + (b * amount) for a, b in zip(position, waypoint))
    return position


def doOperation(position, heading, operation):
    letter = operation[:1]
    amount = int(operation[1:])

    if letter == "F":
        position = move_forward(position, heading, amount)
    elif letter in ["R", "L"]:
        heading = turn(heading, letter, amount)
    else:
        position = move_direction(position, letter, amount)

    return position, heading


def turn(heading, direction, degrees):
    heading = (heading + (DIRECTIONS[direction] * degrees)) % 360
    return heading


def move_forward(position, heading, distance):
    position = tuple(
        a + (b * distance) for a, b in zip(position, DEGREE_VECTORS[heading])
    )
    return position


def move_direction(position, compass, distance):
    position = tuple(
        a + (b * distance)
        for a, b in zip(position, DEGREE_VECTORS[COMPASS_DEGREES[compass]])
    )
    return position
