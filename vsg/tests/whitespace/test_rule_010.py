
import os
import unittest

from vsg.rules import whitespace
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_010_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_010_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_010(self):
        oRule = whitespace.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '010')

        lExpected = [10, 12, 14, 18, 18, 18, 22, 22, 22]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_010(self):
        oRule = whitespace.rule_010()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
