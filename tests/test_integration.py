from src.input_layer import read_mission, parse_mission
from src.logic_layer import execute_instructions

def test_full_pipeline_with_mission_brief():
    mission = read_mission('data/sample.mission')
    expected_output = """1 3 N\n5 1 E"""

    final_positions = [
        execute_instructions(
            rover["position"], 
            rover["instructions"], 
            mission["plateau"]
        ) 
        for rover in mission["rovers"]
    ]

    mission_output = "\n".join(
        f"{rover['x']} {rover['y']} {rover['direction']}" 
        for rover in final_positions
    )

    assert mission_output == expected_output
    
def test_full_pipeline_with_new_data():
    data = """10 10\n0 0 N\nLMRRMMLMM\n10 10 W\nMLRRMRMRRM\n5 5 E\nMRMM"""
    mission = parse_mission(data)
    expected_output = """2 2 N\n9 10 W\n6 3 S"""

    final_positions = [
        execute_instructions(
            rover["position"], 
            rover["instructions"], 
            mission["plateau"]
        ) 
        for rover in mission["rovers"]
    ]

    mission_output = "\n".join(
        f"{rover['x']} {rover['y']} {rover['direction']}" 
        for rover in final_positions
    )

    assert mission_output == expected_output
    