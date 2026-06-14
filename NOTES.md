# Mars Rover Parser Notes

## Input Layer

### Goal

Parse mission information into a structured representation that can be used by the rest of the application.

### Design

Parsing is split into small functions with a single responsibility:

* `parse_plateau`
* `parse_position`
* `parse_instructions`
* `parse_mission`
* `load_mission_from_file`

Responsibilities are separated to keep parsing logic modular and testable.

* `parse_plateau`, `parse_position`, and `parse_instructions` are pure functions.
* `parse_mission` coordinates the parsing process.
* `load_mission_from_file` handles file I/O and delegates parsing to `parse_mission`.

This separation reduces duplication, simplifies testing, and makes it easier to introduce validation and additional features later on.

#### Future Improvements

* Input validation
* Boundary checking
* Custom exceptions for invalid mission files

### Testing

Current coverage includes:

* plateau parsing
* position parsing
* instruction parsing
* full mission parsing

#### Future Test Coverage

* boundary conditions
* invalid input handling
* validation rules


## Logic Layer

### Goal

Take a parsed mission and produce the final positions of each rover.

### Implementation Notes
### Rotation:
- *Input:* `rotate({"x": 0, "y": 0, "direction": "N"}, "L")`

- *Output:* `{"x": 0, "y": 0, "direction": "W"}`
- Needs to take a direction {"N", "E", "S", "W"} and an instruction {"L", "R"}.
- Direction can be considered the current index position in an ordered list.
- The instruction will shift the index position left or right.
- Ordered list needs to behave in a cyclic manner. 

### Movement:
- *Input:* `move({"x": 0, "y": 0, "direction": "N"}, {"max_x": 5, "max_y": 5})`

- *Output:* `{"x": 0, "y": 1, "direction": "N"}`
- Needs to take current position and plateau bounds.
- Checks if a move in the direction will take it out of bounds.
- Returns a new position if the move is legal, or the same position if not.

### Orchestration:
- Takes a list of rover dictionaries
- For each rover loop through valid instructions, either rotate or move.
- Return a list of rover dictionaries with updated final positions

### Assumptions
- Directions are always one of N, E, S, W
- Instructions are always L, R, or M
- Input has already been parsed and validated

### Execution
- Cycles through a full list 
- Checks each instruction type
- Feeds it to the appropriate function (move or rotate)
- Returns final updated position
- Does not mutate the inputs