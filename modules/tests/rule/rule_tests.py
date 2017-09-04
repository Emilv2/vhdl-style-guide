
import sys
sys.path.append('..\..')
import unittest
import rule


class testRuleMethods(unittest.TestCase):

    def test_rule_exists(self):
        oRule = rule.rule()
        self.assertTrue(oRule)

    def test_rule_name(self):
        oRule = rule.rule()
        self.assertFalse(oRule.name)
        oRule.name = 'sName'
        self.assertEqual(oRule.name, 'sName')

    def test_rule_id(self):
        oRule = rule.rule()
        self.assertFalse(oRule.identifier)
        oRule.id = 'rule id 001'
        self.assertEqual(oRule.id, 'rule id 001')

    def test_rule_solution(self):
        oRule = rule.rule()
        self.assertFalse(oRule.solution)
        oRule.solution = 'rule solution'
        self.assertEqual(oRule.solution, 'rule solution')

    def test_add_violations_method(self):
        oRule = rule.rule()
        self.assertEqual(oRule.violations, [])
        oRule.add_violation(1)
        self.assertEqual(oRule.violations, [2])
        oRule.add_violation(10)
        oRule.add_violation(33)
        self.assertEqual(oRule.violations, [2,11,34])


if __name__ == '__main__':
    unittest.main()
