class LRParser:
    def __init__(self):
        # Define the simplified grammar rules
        self.grammar = [
            ("E", ["E", "+", "E"]),  # Rule 1
            ("E", ["id"])            # Rule 2
        ]
        
        # Define the simplified parsing table
        self.action = {
            (0, "id"): ("S", 2),   # Shift and go to state 2
            (0, "+"): None,       # Error
            (1, "$"): ("ACC",),   # Accept
            (2, "+"): ("S", 3),   # Shift and go to state 3
            (2, "$"): ("R", 1),   # Reduce using rule 1 (E -> E + E)
            (3, "id"): ("S", 2),  # Shift and go to state 2
        }
        
        self.goto = {
            (0, "E"): 1,
            (3, "E"): 4
        }
        
        self.stack = [0]  # Initial state
    
    def parse(self, tokens):
        tokens.append("$")  # End of input marker
        index = 0
        
        while True:
            state = self.stack[-1]
            token = tokens[index]
            
            if (state, token) in self.action:
                action, value = self.action[(state, token)]
                
                if action == "S":
                    # Shift operation
                    self.stack.append(value)
                    index += 1
                elif action == "R":
                    # Reduce operation
                    rule = self.grammar[value]
                    for _ in range(len(rule[1])):
                        self.stack.pop()
                    goto_state = self.goto[(self.stack[-1], rule[0])]
                    self.stack.append(goto_state)
                elif action == "ACC":
                    # Accept operation
                    print("Accepted")
                    return True
            else:
                print("Error")
                return False

# Example usage
parser = LRParser()
tokens = ["id", "+", "id"]
if parser.parse(tokens):
    print("Parsing successful.")
else:
    print("Parsing failed.")
