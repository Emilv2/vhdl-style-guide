
import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_007_test_input.vhd'))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed.vhd'), lExpected)


class test_architecture_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_007(self):
        oRule = architecture.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '007')

        lExpected = [11]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_007(self):
        oRule = architecture.rule_007()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
