from src.input_layer import parse_mission
from src.logic_layer import execute_instructions

INPUT = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""

mission = parse_mission(INPUT)

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
