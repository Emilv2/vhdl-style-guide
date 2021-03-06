
from vsg import rule
from vsg import utils


class rule_007(rule.rule):
    '''
    Signal rule 007 checks for default assignments in signal declarations.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'signal', '007')
        self.solution = 'Remove default assignment.'
        self.phase = 1
        self.fixable = False  # Allow the user to decide if these should be removed

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isSignal and ':=' in oLine.line:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)
