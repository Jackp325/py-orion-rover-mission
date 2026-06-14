


DIRECTIONS = ["N", "E", "S", "W"]
ROTATE_MAP = {"L": -1, "R": 1}

def rotate(position, instruction):
    idx = DIRECTIONS.index(position["direction"])
    new_idx = (idx + ROTATE_MAP[instruction]) % len(DIRECTIONS)

    return {
        "x": position["x"],
        "y": position["y"],
        "direction": DIRECTIONS[new_idx]
    }

MOVE_MAP = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0)
}

def move(position, plateau):
    dx, dy = MOVE_MAP[position["direction"]]
    x = position["x"] + dx
    y = position["y"] + dy
    if 0 <= x <= plateau["max_x"] and 0 <= y <= plateau["max_y"]:
        return {
            "x": x,
            "y": y,
            "direction": position["direction"]
        }
    else:
        return {
            "x": position["x"],
            "y": position["y"],
            "direction": position["direction"]
        }