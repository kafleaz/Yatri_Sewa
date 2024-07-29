# Define the grammar rules
# Example grammar: 
# S -> AB 
# A -> aA | ε 
# B -> bB | ε 
grammar = { 
    'S': [['A', 'B']], 
    'A': [['a', 'A'], ['ε']], 
    'B': [['b', 'B'], ['ε']] 
} 

# Initialize the FIRST set
first = {non_terminal: set() for non_terminal in grammar}

# Function to compute the FIRST set for a given non-terminal
def compute_first(non_terminal):
    # If FIRST is already computed, return it
    if first[non_terminal]:
        return first[non_terminal]
    
    # Process each production rule
    for production in grammar[non_terminal]:
        for symbol in production:
            if symbol.islower():  # Terminal symbol
                first[non_terminal].add(symbol)
                break
            elif symbol == 'ε':  # Epsilon
                first[non_terminal].add('ε')
                break
            else:  # Non-terminal symbol
                first_set = compute_first(symbol)
                if 'ε' in first_set:
                    first[non_terminal].update(first_set - {'ε'})
                else:
                    first[non_terminal].update(first_set)
                    break
        else:
            first[non_terminal].add('ε')
    
    return first[non_terminal]

# Compute the FIRST set for all non-terminals
for non_terminal in grammar:
    compute_first(non_terminal)

# Print the FIRST sets
for non_terminal, first_set in first.items():
    print(f'FIRST({non_terminal}) = {{ {", ".join(first_set)} }}')
