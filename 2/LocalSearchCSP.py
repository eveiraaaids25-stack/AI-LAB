"""
EX.NO: 2  IMPLEMENT LOCAL SEARCH ALGORITHM FOR CSP
AIM: To write a simple program to implement local search for CSP (N-Queens, min-conflicts).
"""

import random


class NQueensCSP:
    def __init__(self, N):
        self.N = N
        self.domains = list(range(N))

    def conflicts(self, assignment):
        """Returns the number of conflicts in the current assignment."""
        count = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if assignment[i] == assignment[j] or abs(assignment[i] - assignment[j]) == j - i:
                    count += 1
        return count

    def var_conflicts(self, assignment, var):
        """Returns the number of other queens that conflict with the queen in column `var`."""
        count = 0
        for other in range(self.N):
            if other != var and (assignment[var] == assignment[other]
                                 or abs(assignment[var] - assignment[other]) == abs(var - other)):
                count += 1
        return count

    def min_conflicts(self, max_steps=1000):
        """Min-Conflicts algorithm to solve the N-Queens problem."""
        assignment = [random.choice(self.domains) for _ in range(self.N)]

        for _ in range(max_steps):
            if self.conflicts(assignment) == 0:
                return assignment

            # Pick a random variable that is actually in conflict
            conflicted_vars = [i for i in range(self.N) if self.var_conflicts(assignment, i) > 0]
            var = random.choice(conflicted_vars)

            # Move it to a different value with the fewest conflicts (break ties randomly)
            scores = {val: self.conflicts(assignment[:var] + [val] + assignment[var + 1:])
                      for val in self.domains if val != assignment[var]}
            best = min(scores.values())
            assignment[var] = random.choice([val for val, sc in scores.items() if sc == best])
        return None


if __name__ == "__main__":
    N = 8
    nqueens = NQueensCSP(N)
    solution = nqueens.min_conflicts()
    if solution:
        print("Solution found:", solution)
    else:
        print("No solution found within the maximum number of steps")
