"""
EX.NO: 6(b)  IMPLEMENT BACKWARD CHAINING STRATEGY
AIM: To write a program for backward chaining strategy.
"""


class BackwardChaining:
    def __init__(self, rules, facts):
        self.rules = rules
        self.facts = facts

    def is_known(self, fact):
        return fact in self.facts

    def infer(self, goal):
        if self.is_known(goal):
            return True
        for rule in self.rules:
            if goal in rule["then"] and all(self.infer(premise) for premise in rule["if"]):
                self.facts.update(rule["then"])
                return True
        return False


if __name__ == "__main__":
    rules = [
        {"if": {"A"}, "then": {"B"}},
        {"if": {"B"}, "then": {"C"}},
        {"if": {"C"}, "then": {"D"}}
    ]
    facts = {"A"}

    bc = BackwardChaining(rules, facts)
    goal = "D"
    can_infer = bc.infer(goal)
    print(f"Can infer {goal}:", can_infer)
    print("Known facts:", bc.facts)
