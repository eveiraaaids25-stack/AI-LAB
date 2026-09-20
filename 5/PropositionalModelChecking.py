"""
EX.NO: 5(b)  IMPLEMENT PROPOSITIONAL MODEL CHECKING ALGORITHM
AIM: To implement propositional model checking algorithm (DPLL).
"""


def find_unit_clause(clauses):
    """Finds a unit clause in the list of clauses."""
    for clause in clauses:
        if len(clause) == 1:
            return clause[0]
    return None


def simplify_clauses(clauses, literal):
    """Simplifies the list of clauses by setting the given literal to True."""
    simplified = []
    for clause in clauses:
        if literal in clause:
            continue  # Clause is satisfied
        new_clause = [l for l in clause if l != -literal]
        if not new_clause:
            return None  # Clause is unsatisfiable
        simplified.append(new_clause)
    return simplified


def dpll(clauses, assignments):
    """Implements the DPLL algorithm for propositional model checking."""
    # Unit propagation
    unit = find_unit_clause(clauses)
    while unit is not None:
        assignments.append(unit)
        clauses = simplify_clauses(clauses, unit)
        if clauses is None:
            return False
        unit = find_unit_clause(clauses)

    if not clauses:
        return True  # All clauses satisfied

    # Choose a literal and try True, then False, backtracking on failure
    literal = clauses[0][0]
    mark = len(assignments)

    new_clauses = simplify_clauses(clauses, literal)
    if new_clauses is not None:
        assignments.append(literal)
        if dpll(new_clauses, assignments):
            return True
        del assignments[mark:]

    new_clauses = simplify_clauses(clauses, -literal)
    if new_clauses is not None:
        assignments.append(-literal)
        if dpll(new_clauses, assignments):
            return True
        del assignments[mark:]

    return False


def main():
    # Example: (A or B) and (not A or C) and (not B or not C)
    # Represented as CNF: [[A, B], [-A, C], [-B, -C]]
    A, B, C = 1, 2, 3  # Literal encoding
    clauses = [[A, B], [-A, C], [-B, -C]]

    assignments = []
    if dpll(clauses, assignments):
        print("SATISFIABLE with assignments:", assignments)
    else:
        print("UNSATISFIABLE")


if __name__ == "__main__":
    main()
