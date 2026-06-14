from src.input_layer import load_mission
from src.logic_layer import run_mission

mission = load_mission('data/sample.mission')
mission_output = run_mission(mission)

print(mission_output)
