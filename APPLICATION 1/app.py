# app.py
from flask import Flask, render_template, request, jsonify
from ast_engine import create_rule, evaluate_rule
from database.db import init_db, add_rule, get_rules, update_rule, delete_rule

app = Flask(__name__)

@app.before_request
def setup():
    """Initialize the database when the app starts."""
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/evaluate_rule', methods=['POST'])
def evaluate():
    data = request.json
    rule_string = data.get("rule")
    
    # Validate incoming data
    if not rule_string:
        return jsonify(result="Error: Rule string is required."), 400

    user_data = {
        "age": int(data.get("age", 0)),  # Default to 0 if not provided
        "department": data.get("department", ""),
        "salary": int(data.get("salary", 0)),  # Default to 0 if not provided
        "experience": int(data.get("experience", 0))  # Default to 0 if not provided
    }

    validation_error = validate_user_data(user_data)
    if validation_error:
        return jsonify(result=f"Error: {validation_error}"), 400

    try:
        rule_ast = create_rule(rule_string)
        if not rule_ast:
            return jsonify(result="Error: Invalid rule format."), 400
        
        add_rule(rule_string, str(rule_ast))  # Store rule in the database
        result = evaluate_rule(rule_ast, user_data)
        return jsonify(result=result)
    
    except Exception as e:
        return jsonify(result=f"Error during evaluation: {str(e)}"), 500

@app.route('/api/rules', methods=['GET'])
def get_all_rules():
    """Endpoint to retrieve all stored rules."""
    rules = get_rules()
    return jsonify(rules=rules)

@app.route('/api/update_rule/<int:rule_id>', methods=['PUT'])
def update_existing_rule(rule_id):
    data = request.json
    new_rule_string = data.get("rule")
    
    # Validate incoming data
    if not new_rule_string:
        return jsonify(result="Error: New rule string is required."), 400

    try:
        new_ast = create_rule(new_rule_string)
        if not new_ast:
            return jsonify(result="Error: Invalid new rule format."), 400
        
        update_rule(rule_id, new_rule_string, str(new_ast))  # Update rule in the database
        return jsonify(result="Rule updated successfully.")
    
    except Exception as e:
        return jsonify(result=f"Error during update: {str(e)}"), 500

@app.route('/api/delete_rule/<int:rule_id>', methods=['DELETE'])
def delete_existing_rule(rule_id):
    try:
        delete_rule(rule_id)  # Delete rule from the database
        return jsonify(result="Rule deleted successfully.")
    
    except Exception as e:
        return jsonify(result=f"Error during deletion: {str(e)}"), 500

def validate_user_data(user_data):
    """Validate user attributes."""
    if user_data['age'] < 0:
        return "Invalid age"
    if not user_data['department']:
        return "Department cannot be empty"
    if user_data['salary'] < 0:
        return "Invalid salary"
    if user_data['experience'] < 0:
        return "Invalid experience"
    return None

if __name__ == '__main__':
    app.run(debug=True)
