import unittest
import json

from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils


class testVsg(unittest.TestCase):

    def test_extract_violation_dictionary(self):
        lFile = []
        utils.read_file('vsg/tests/code_examples/spi_master.vhd', lFile)
        oFile = vhdlFile.vhdlFile(lFile)
        oRules = rule_list.rule_list(oFile)
        oRules.check_rules()
        with open('vsg/tests/rule_list/extract_violation_dictionary.json') as jsonFile:
            dExpected = json.load(jsonFile)
        self.assertEqual(dExpected, oRules.extract_violation_dictionary())
        
    def test_extract_violation_dictionary_w_all_phases_enabled(self):
        lFile = []
        utils.read_file('vsg/tests/code_examples/spi_master.vhd', lFile)
        oFile = vhdlFile.vhdlFile(lFile)
        oRules = rule_list.rule_list(oFile)
        oRules.check_rules(True)
        with open('vsg/tests/rule_list/extract_violation_dictionary_w_all_phases_enabled.json') as jsonFile:
            dExpected = json.load(jsonFile)
        self.assertEqual(dExpected, oRules.extract_violation_dictionary())
        

