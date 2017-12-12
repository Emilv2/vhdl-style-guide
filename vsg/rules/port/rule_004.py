
from vsg import rule
from vsg import check
from vsg import fix


class rule_004(rule.rule):
    '''
    Port rule 004 checks indentation of ports.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'port'
        self.identifier = '004'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and not oLine.isEndPortMap:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.indent(self, oFile.lines[iLineNumber])