"""
EX.NO: 6(a)  IMPLEMENT FORWARD CHAINING STRATEGY
AIM: To write a program for forward chaining strategy.
"""


class ForwardChaining:
    def __init__(self, rules, facts):
        self.rules = rules
        self.facts = facts

    def apply_rules(self):
        inferred = set(self.facts)
        new_inferred = True
        while new_inferred:
            new_inferred = False
            for rule in self.rules:
                if rule["if"].issubset(inferred) and not rule["then"].issubset(inferred):
                    inferred.update(rule["then"])
                    new_inferred = True
        return inferred


if __name__ == "__main__":
    rules = [
        {"if": {"A"}, "then": {"B"}},
        {"if": {"B"}, "then": {"C"}},
        {"if": {"C"}, "then": {"D"}}
    ]
    facts = {"A"}

    fc = ForwardChaining(rules, facts)
    inferred_facts = fc.apply_rules()
    print("Inferred facts:", inferred_facts)
