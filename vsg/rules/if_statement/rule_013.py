
from vsg import rule
from vsg import utilities

import re


class rule_013(rule.rule):
    '''If rule 013 checks the "else" keyword is on it's own line.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'if'
        self.identifier = '013'
        self.solution = 'Move "else" keyword to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isElseKeyword and not re.match('^\s*else', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utilities.split_line_before_word(oFile, iLineNumber, ' else')
            oFile.lines[iLineNumber].isElseKeyword = False
            oFile.lines[iLineNumber + 1].isIfKeyword = False
            oFile.lines[iLineNumber + 1].isElseIfKeyword = False
            oFile.lines[iLineNumber + 1].isThenKeyword = False
            oFile.lines[iLineNumber + 1].indentLevel -= 1