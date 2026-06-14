from src.input_layer import load_mission, parse_mission
from src.logic_layer import run_mission

def test_full_pipeline_with_mission_brief():
    mission = load_mission('data/sample.mission')
    expected_output = """1 3 N\n5 1 E"""

    mission_output = run_mission(mission)

    assert mission_output == expected_output
    
def test_full_pipeline_with_new_data():
    data = """10 10\n0 0 N\nLMRRMMLMM\n10 10 W\nMLRRMRMRRM\n5 5 E\nMRMM"""
    mission = parse_mission(data)
    expected_output = """2 2 N\n9 10 W\n6 3 S"""

    mission_output = run_mission(mission)

    assert mission_output == expected_output
    