

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
    return list(text)

def parse_mission(text):
    pass