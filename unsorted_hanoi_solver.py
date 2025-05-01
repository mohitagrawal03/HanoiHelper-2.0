from typing import List, Tuple, Dict, Set
import copy

TOWERS = ['A', 'B', 'C']

Move = Tuple[str, str]

class HanoiSolver:
    def __init__(self, initial_stack: List[int]):
        self.initial_state = {
            'A': initial_stack[::-1],
            'B': [],
            'C': []
        }
        self.goal_state = {
            'A': [],
            'B': sorted(initial_stack)[::-1],
            'C': []
        }
        self.num_disks = len(initial_stack)
        self.visited_states: Set[str] = set()
        self.solution_moves: List[Move] = []

    def is_goal(self, state: Dict[str, List[int]]) -> bool:
        return state == self.goal_state

    def encode_state(self, state: Dict[str, List[int]]) -> str:
        return '|'.join(','.join(map(str, state[tower])) for tower in TOWERS)

    def get_top(self, state: Dict[str, List[int]], tower: str) -> int:
        return state[tower][-1] if state[tower] else float('inf')

    def generate_moves(self, state: Dict[str, List[int]]) -> List[Move]:
        moves = []
        for from_tower in TOWERS:
            if not state[from_tower]:
                continue
            disk = state[from_tower][-1]
            for to_tower in TOWERS:
                if from_tower == to_tower:
                    continue
                if not state[to_tower] or disk < state[to_tower][-1]:
                    moves.append((from_tower, to_tower))
        return moves

    def apply_move(self, state: Dict[str, List[int]], move: Move) -> Dict[str, List[int]]:
        from_tower, to_tower = move
        new_state = copy.deepcopy(state)
        disk = new_state[from_tower].pop()
        new_state[to_tower].append(disk)
        return new_state

    def dfs(self, state: Dict[str, List[int]], path: List[Move]) -> bool:
        encoded = self.encode_state(state)
        if encoded in self.visited_states:
            return False
        self.visited_states.add(encoded)

        if self.is_goal(state):
            self.solution_moves = path
            return True

        for move in self.generate_moves(state):
            next_state = self.apply_move(state, move)
            if self.dfs(next_state, path + [move]):
                return True

        return False

    def solve(self) -> List[Move]:
        print(f"Solving Hanoi with initial state: {self.initial_state}")
        found = self.dfs(self.initial_state, [])
        if not found:
            print("No solution found.")
        return self.solution_moves

# === Sample Run ===
if __name__ == "__main__":
    initial_disks = [3, 4, 0, 2, 1]
    solver = HanoiSolver(initial_disks)
    moves = solver.solve()
    print("\nSteps to solve:")
    for i, (from_tower, to_tower) in enumerate(moves, 1):
        print(f"Step {i}: Move disk from {from_tower} to {to_tower}")
    print(f"\nTotal moves: {len(moves)}")
