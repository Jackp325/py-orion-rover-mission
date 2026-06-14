


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
