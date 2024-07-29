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

# Initialize the FOLLOW set
follow = {non_terminal: set() for non_terminal in grammar}
follow['S'].add('$')  # End of input symbol for the start symbol

# Function to compute the FOLLOW set for all non-terminals
def compute_follow():
    while True:
        updated = False
        for non_terminal, productions in grammar.items():
            for production in productions:
                trailer = follow[non_terminal].copy()
                for symbol in reversed(production):
                    if symbol in grammar:  # Non-terminal
                        if follow[symbol] != follow[symbol].union(trailer):
                            follow[symbol].update(trailer)
                            updated = True
                        if 'ε' in first[symbol]:
                            trailer.update(first[symbol] - {'ε'})
                        else:
                            trailer = first[symbol].copy()
                    else:  # Terminal
                        trailer = {symbol}
        if not updated:
            break

# Compute the FOLLOW sets
compute_follow()

# Print the FOLLOW sets
for non_terminal, follow_set in follow.items():
    print(f'FOLLOW({non_terminal}) = {{ {", ".join(follow_set)} }}')
