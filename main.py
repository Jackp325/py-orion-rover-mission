from src.input_layer import read_mission
from src.logic_layer import execute_instructions

mission = read_mission('data/sample.mission')

plateau = mission["plateau"]
rovers = mission["rovers"]

final_positions = [
    execute_instructions(
        rover["position"], 
        rover["instructions"], 
        plateau
    ) 
    for rover in rovers
]

mission_output = "\n".join(
    f"{rover['x']} {rover['y']} {rover['direction']}" 
    for rover in final_positions
)

print(mission_output)
