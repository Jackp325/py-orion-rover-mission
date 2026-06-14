


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

    new_x = position["x"] + dx
    new_y = position["y"] + dy

    if 0 <= new_x <= plateau["max_x"] and 0 <= new_y <= plateau["max_y"]:
        x = new_x
        y = new_y
    else:
        x = position["x"]
        y = position["y"]

    return {
        "x": x,
        "y": y,
        "direction": position["direction"]
    }

def execute_instructions(position, instructions, plateau):
    current_position = position
    for instruction in instructions:
        if instruction == "M":
            current_position = move(current_position, plateau)
        else:
            current_position = rotate(current_position, instruction)
    return current_position

def run_mission(mission):
    final_positions = [
        execute_instructions(
            rover["position"], 
            rover["instructions"], 
            mission["plateau"]
        ) 
        for rover in mission["rovers"]
    ]
    
    return "\n".join(
        f"{rover['x']} {rover['y']} {rover['direction']}" 
        for rover in final_positions
    )