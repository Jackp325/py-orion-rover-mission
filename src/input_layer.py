

def read_mission(path):
    with open(path, "r") as file:
        mission_text = file.read()

    return parse_mission(mission_text)

def parse_plateau(text):
    max_x, max_y = map(int, text.split())
    return {"max_x": max_x, "max_y": max_y}

def parse_position(text):
    x, y, direction = text.split()
    return {
        "x": int(x), 
        "y": int(y), 
        "direction": direction
    }

def parse_instructions(text):
    return list(text.strip())

def parse_mission(text):
    lines = text.strip().splitlines()

    plateau_line = lines[0]
    rover_list = []
    for i in range(1, len(lines), 2):
        position_line = lines[i]
        instructions_line = lines[i + 1]
        rover_list.append({
                "position": parse_position(position_line),
                "instructions": parse_instructions(instructions_line)
        })

    return {
        "plateau": parse_plateau(plateau_line),
        "rovers": rover_list
    }