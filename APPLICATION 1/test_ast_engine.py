# test_ast_engine.py

import unittest
from ast_engine import create_rule, evaluate_rule, Node

class TestRuleEngine(unittest.TestCase):
    
    def test_create_rule_and(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.type, 'operator')
        self.assertEqual(ast.value, 'AND')
        self.assertEqual(ast.left.value, "age > 30")
        self.assertEqual(ast.right.value, "department = 'Sales'")

    def test_evaluate_rule_true(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 5}
        result = evaluate_rule(ast, user_data)
        self.assertTrue(result)

    def test_evaluate_rule_false(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        user_data = {"age": 25, "department": "Marketing", "salary": 40000, "experience": 2}
        result = evaluate_rule(ast, user_data)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
