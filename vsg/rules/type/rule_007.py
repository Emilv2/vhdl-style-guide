
from vsg import rule
from vsg import fix

import re


class rule_007(rule.rule):
    '''
    Type rule 007 checks for a single space after the "is" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'type'
        self.identifier = '007'
        self.solution = 'Ensure a single space after the "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                if not re.match('^.*\sis\s\S', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'is')