

def parse_plateau(text):
    x, y = map(int, text.split())
    return {"max_x": x, "max_y": y}