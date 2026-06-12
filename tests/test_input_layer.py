from src.input_layer import parse_plateau

def test_parse_plateau_valid_inputs_return_correct_dict():
    plateau_1 = "5 5"
    plateau_2 = "10 10"

    assert parse_plateau(plateau_1) == {"max_x": 5, "max_y": 5}
    assert parse_plateau(plateau_2) == {"max_x": 10, "max_y": 10}