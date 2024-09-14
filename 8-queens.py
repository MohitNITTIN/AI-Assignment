import random


class EightQueens:
    def __init__(self):
        # Initialize a random board configuration
        self.board = self.random_board()

    def random_board(self):
        # Generate a random board with one queen in each row
        return [random.randint(0, 7) for _ in range(8)]

    def calculate_conflicts(self):
        # Calculate the number of conflicts in the current board
        conflicts = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if self.board[i] == self.board[j]:  # Same column
                    conflicts += 1
                if abs(self.board[i] - self.board[j]) == abs(i - j):  # Same diagonal
                    conflicts += 1
        return conflicts

    def get_neighbors(self):
        # Generate all possible neighbor states by moving each queen
        neighbors = []
        for row in range(8):
            for col in range(8):
                if col != self.board[row]:  # Move queen to a different column
                    new_board = self.board[:]
                    new_board[row] = col
                    neighbors.append(new_board)
        return neighbors

    def first_choice_hill_climbing(self):
        current_conflicts = self.calculate_conflicts()
        while current_conflicts > 0:
            neighbors = self.get_neighbors()
            next_board = None
            next_conflicts = float('inf')

            for neighbor in neighbors:
                self.board = neighbor
                conflict_count = self.calculate_conflicts()
                if conflict_count < next_conflicts:
                    next_conflicts = conflict_count
                    next_board = neighbor
                    if next_conflicts == 0:  # Found a solution
                        break

            if next_board is None or next_conflicts >= current_conflicts:
                break  # No better neighbor found, stop the search

            self.board = next_board
            current_conflicts = next_conflicts

        return self.board if current_conflicts == 0 else None


def main():
    solver = EightQueens()
    solution = solver.first_choice_hill_climbing()

    if solution:
        print("Solution found:")
        for row in range(8):
            line = ['.'] * 8
            line[solution[row]] = 'Q'
            print(" ".join(line))
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
