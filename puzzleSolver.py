"""
simple brute force solver for a specific type of game puzzle that offten involves buttons and plataforms
"""
from itertools import product
from typing import List, Dict, Optional, Tuple


class PlatformPuzzle:
    def __init__(self, platform_count: int, levels: int, buttons: Dict[int, List[int]], initial_state: List[int]):
        """
        Initializes the platform puzzle.

        :param platform_count: Number of platforms in the puzzle.
        :param levels: Number of levels each platform can be in (0 to levels - 1).
        :param buttons: Mapping of button numbers to the platforms they affect.
        :param initial_state: Starting configuration of the platforms.
        """
        self.platform_count = platform_count
        self.levels = levels
        self.buttons = buttons
        self.initial_state = initial_state

    def apply_button(self, state: List[int], button: int) -> List[int]:
        """
        Simulates pressing a button and returns the new state of the platforms.

        :param state: Current state of the platforms.
        :param button: Button number to press.
        :return: Updated state of the platforms.
        """
        new_state = state[:]
        for platform in self.buttons.get(button, []):
            new_state[platform] = (new_state[platform] + 1) % self.levels
        return new_state

    def brute_force_solution(self, target_state: List[int], max_length: int = 10) -> Optional[Tuple[int, ...]]:
        """
        Brute forces the puzzle to find a sequence of button presses to reach the target state.

        :param target_state: Desired target state of the platforms.
        :param max_length: Maximum length of the button press sequence to consider.
        :return: A tuple of button presses if a solution is found, otherwise None.
        """
        for length in range(1, max_length + 1):
            for sequence in product(self.buttons.keys(), repeat=length):
                state = self.initial_state[:]
                for button in sequence:
                    state = self.apply_button(state, button)
                if state == target_state:
                    return sequence
        return None


def main():
    # Puzzle configuration
    platform_count = 5
    levels = 3
    buttons = {
        1: [0, 2],  # Button 1 moves platforms 1 and 3 (indices 0 and 2)
        2: [1, 2],  # Button 2 moves platforms 2 and 3 (indices 1 and 2)
        3: [3, 4],  # Button 3 moves platforms 4 and 5 (indices 3 and 4)
        4: [0, 4],  # Button 4 moves platforms 1 and 5 (indices 0 and 4)
    }
    initial_state = [1, 0, 2, 1, 0]  # Example initial configuration of platforms
    target_state = [0] * platform_count  # Target is all platforms at level 0

    # Solve the puzzle
    puzzle = PlatformPuzzle(platform_count, levels, buttons, initial_state)
    solution = puzzle.brute_force_solution(target_state)

    # Output the result
    if solution:
        print(f"Solution found: Press buttons {solution}")
    else:
        print("No solution found within the search limit.")


if __name__ == "__main__":
    main()
