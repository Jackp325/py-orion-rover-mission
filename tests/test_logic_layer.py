from src.logic_layer import rotate, move, execute_instructions

def test_rotate_left_from_north_returns_west():
    position = {"x": 0, "y": 0, "direction": "N"}
    instruction = "L"
    expected_direction = "W"

    result = rotate(position, instruction)

    assert result["direction"] == expected_direction

def test_rotate_does_not_mutate_position():
    position = {"x": 0, "y": 0, "direction": "N"}
    instruction = "L"

    result = rotate(position, instruction)

    assert (result["x"], result["y"]) == (position["x"], position["y"])

def test_rotate_in_all_directions():
    test_cases = {
        ("N", "L"): "W",
        ("W", "L"): "S",
        ("S", "L"): "E",
        ("E", "L"): "N",
        ("N", "R"): "E",
        ("E", "R"): "S",
        ("S", "R"): "W",
        ("W", "R"): "N",
    }
    for (start, instruction), expected in test_cases.items():
        result = rotate({"x": 0, "y": 0, "direction": start}, instruction)
        assert result["direction"] == expected, f"{start} + {instruction} failed"

def test_rotate_left_four_times_returns_to_starting_position():
    position = {"x": 0, "y": 0, "direction": "N"}
    instruction = "L"
    expected_result = "N"

    for _ in range(4):
        position = rotate(position, instruction)

    assert position["direction"] == expected_result


def test_move_north_increases_y_by_one():
    position = {"x": 0, "y": 0, "direction": "N"}
    plateau = {"max_x": 5, "max_y": 5}
    expected_result = {"x": 0, "y": 1, "direction": "N"}
    
    result = move(position, plateau)

    assert result == expected_result

def test_move_east_increases_x_by_one():
    position = {"x": 0, "y": 0, "direction": "E"}
    plateau = {"max_x": 5, "max_y": 5}
    expected_result = {"x": 1, "y": 0, "direction": "E"}
    
    result = move(position, plateau)

    assert result == expected_result

def test_move_south_out_of_bounds_does_not_move():
    position = {"x": 0, "y": 0, "direction": "S"}
    plateau = {"max_x": 5, "max_y": 5}
    expected_result = {"x": 0, "y": 0, "direction": "S"}

    result = move(position, plateau)

    assert result == expected_result

def test_move_west_out_of_bounds_does_not_move():
    position = {"x": 0, "y": 0, "direction": "W"}
    plateau = {"max_x": 5, "max_y": 5}
    expected_result = {"x": 0, "y": 0, "direction": "W"}
    
    result = move(position, plateau)

    assert result == expected_result

def test_move_north_out_of_bounds_does_not_move():
    position = {"x": 0, "y": 5, "direction": "N"}
    plateau = {"max_x": 5, "max_y": 5}
    expected_result = {"x": 0, "y": 5, "direction": "N"}

    result = move(position, plateau)

    assert result == expected_result

def test_move_east_out_of_bounds_does_not_move():
    position = {"x": 5, "y": 0, "direction": "E"}
    plateau = {"max_x": 5, "max_y": 5}
    expected_result = {"x": 5, "y": 0, "direction": "E"}

    result = move(position, plateau)

    assert result == expected_result


def test_execute_instructions_no_instruction_returns_starting_position():
    position = {"x": 1, "y": 2, "direction": "N"}
    instructions = []
    plateau = {"max_x": 5, "max_y": 5}
    expected_result = {"x": 1, "y": 2, "direction": "N",}

    result = execute_instructions(position, instructions, plateau)

    assert result == expected_result

def test_execute_instructions_single_move_applies_correctly():
    position = {"x": 1, "y": 2, "direction": "N"}
    instructions = ["M"]
    plateau = {"max_x": 5, "max_y": 5}

    result = execute_instructions(position, instructions, plateau)

    assert result["y"] == 3

def test_execute_instructions_single_rotate_applies_correctly():
    position = {"x": 1, "y": 2, "direction": "N"}
    instructions = ["L"]
    plateau = {"max_x": 5, "max_y": 5}

    result = execute_instructions(position, instructions, plateau)

    assert result["direction"] == "W"

def test_execute_instructions_does_not_mutate_starting_position():
    starting_position = {"x": 1, "y": 2, "direction": "N"}
    instructions = ["M"]
    plateau = {"max_x": 5, "max_y": 5}

    original_position = starting_position.copy()

    execute_instructions(starting_position, instructions, plateau)

    assert starting_position == original_position

def test_execute_instructions_handles_full_instruction_list():
    position = {"x": 1, "y": 2, "direction": "N"}
    instructions = ["L", "M", "L", "M", "L", "M", "L", "M", "M"]
    plateau = {"max_x": 5, "max_y": 5}
    expected_result = {"x": 1, "y": 3, "direction": "N"}

    result = execute_instructions(position, instructions, plateau)

    assert result == expected_result