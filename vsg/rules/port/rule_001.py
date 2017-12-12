
from vsg import rule
from vsg import check


class rule_001(rule.rule):
    '''
    Port rule 001 checks for a blank line above the port keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'port'
        self.identifier = '001'
        self.solution = 'Remove blank lines above "port" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                check.is_no_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            while oFile.lines[iLineNumber - 1].isBlank:
                oFile.lines.pop(iLineNumber - 1)