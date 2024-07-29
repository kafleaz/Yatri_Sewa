class IntermediateCodeGenerator:
    def __init__(self):
        self.temp_counter = 0
        self.instructions = []
        self.label_counter = 0

    def generate_temp(self):
        """Generate a new temporary variable name."""
        self.temp_counter += 1
        return f"t{self.temp_counter - 1}"

    def generate_label(self):
        """Generate a new label name."""
        self.label_counter += 1
        return f"L{self.label_counter - 1}"

    def add_instruction(self, instruction):
        """Add an instruction to the list of instructions."""
        self.instructions.append(instruction)

    def generate_code(self, ast):
        """Generate intermediate code from the AST."""
        self.visit(ast)
        return self.instructions

    def visit(self, node):
        """Visit a node in the AST."""
        if isinstance(node, BinOp):
            return self.visit_binop(node)
        elif isinstance(node, Num):
            return node.value
        elif isinstance(node, Variable):
            return node.name

    def visit_binop(self, node):
        """Handle binary operations."""
        left = self.visit(node.left)
        right = self.visit(node.right)
        result = self.generate_temp()
        self.add_instruction(f"{result} = {left} {node.op} {right}")
        return result

class ASTNode:
    """Base class for all AST nodes."""
    pass

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(ASTNode):
    def __init__(self, value):
        self.value = value

class Variable(ASTNode):
    def __init__(self, name):
        self.name = name

# Example usage
if __name__ == "__main__":
    # Constructing AST for the expression: (2 + 6) * 3
    ast = BinOp(
        left=BinOp(left=Num(2), op='+', right=Num(6)),
        op='*',
        right=Num(3)
    )

    # Generate intermediate code
    generator = IntermediateCodeGenerator()
    intermediate_code = generator.generate_code(ast)

    # Print intermediate code
    for instruction in intermediate_code:
        print(instruction)
