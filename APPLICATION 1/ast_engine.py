# ast_engine.py

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type    # 'operator' or 'operand'
        self.left = left         # left child node
        self.right = right       # right child node
        self.value = value       # operand value (like age, department)

    def __repr__(self):
        return f"Node({self.type}, {self.value}, left={self.left}, right={self.right})"


# Function to create the AST based on rule string
def create_rule(rule_string):
    """
    This function parses the rule string and creates an AST representation.
    Right now, it only supports AND-based rules.
    """
    if 'AND' in rule_string:
        conditions = rule_string.split(' AND ')
        left_condition = conditions[0].strip()  # E.g., "age > 30"
        right_condition = conditions[1].strip()  # E.g., "department = 'Sales'"
        
        # Create operand nodes for both conditions
        left_node = Node(node_type='operand', value=left_condition)
        right_node = Node(node_type='operand', value=right_condition)
        
        # Return the operator node combining the two operand nodes
        return Node(node_type='operator', left=left_node, right=right_node, value='AND')
    
    return None  # If the rule doesn't match the expected pattern, return None


# Function to evaluate the AST against user data
def evaluate_rule(ast, user_data):
    if ast.type == 'operand':
        # Check the operator in the condition
        if '>' in ast.value:
            # Format: age > 30
            var, threshold = ast.value.split('>')
            var = var.strip()  # e.g., "age"
            threshold = threshold.strip()  # e.g., "30"
            return user_data[var] > int(threshold)
        
        elif '<' in ast.value:
            # Format: age < 30
            var, threshold = ast.value.split('<')
            var = var.strip()  # e.g., "age"
            threshold = threshold.strip()  # e.g., "30"
            return user_data[var] < int(threshold)
        
        elif '=' in ast.value:
            # Format: department = 'Sales'
            var, val = ast.value.split('=')
            var = var.strip()  # e.g., "department"
            val = val.strip().strip("'")  # e.g., "Sales"
            return user_data[var] == val
        
    elif ast.type == 'operator':
        if ast.value == 'AND':
            return evaluate_rule(ast.left, user_data) and evaluate_rule(ast.right, user_data)
        elif ast.value == 'OR':
            return evaluate_rule(ast.left, user_data) or evaluate_rule(ast.right, user_data)

    return None
