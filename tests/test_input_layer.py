from src.input_layer import parse_plateau, parse_position, parse_instructions

def test_parse_plateau_valid_inputs_return_correct_dict():
    plateau_1 = "5 5"
    plateau_2 = "10 10"

    assert parse_plateau(plateau_1) == {"max_x": 5, "max_y": 5}
    assert parse_plateau(plateau_2) == {"max_x": 10, "max_y": 10}


def test_parse_position_valid_inputs_return_correct_dict():
    rover_1 = "1 2 N"
    rover_2 = "5 7 S"
    rover_3 = "3 1 E"
    rover_4 = "0 0 W"

    assert parse_position(rover_1) == {"x": 1, "y": 2, "direction": "N"}
    assert parse_position(rover_2) == {"x": 5, "y": 7, "direction": "S"}
    assert parse_position(rover_3) == {"x": 3, "y": 1, "direction": "E"}
    assert parse_position(rover_4) == {"x": 0, "y": 0, "direction": "W"}


def test_parse_intructions_returns_a_list():
    assert parse_instructions("") == []

def test_parse_intructions_single_instruction_returns_a_list_of_one():
    assert parse_instructions("L") == ["L"]

def test_parse_intructions_multiple_instruction_returns_in_correct_order():
    assert parse_instructions("LMLMLMLMM") == ["L", "M", "L", "M", "L", "M", "L", "M", "M"]