from test_logic_layer import rotate

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
    for _ in range(4):
        position = rotate(position, instruction)

    assert position["direction"] == "N"