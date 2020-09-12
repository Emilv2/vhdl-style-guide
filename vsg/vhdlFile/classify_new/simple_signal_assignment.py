
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import simple_force_assignment
from vsg.vhdlFile.classify_new import simple_release_assignment
#from vsg.vhdlFile.classify_new import simple_waveform_assignment

'''
    simple_signal_assignment ::=
        simple_waveform_assignment
      | simple_force_assignment
      | simple_release_assignment
'''

def detect(iToken, lObjects):

    if utils.find_in_range('<=', iToken, ';', lObjects):
        if utils.find_in_range('when', iToken, ';', lObjects):
            return False
        if utils.find_in_range('with', iToken, ';', lObjects):
            return False
        return True
    return False


def classify(iToken, lObjects):

    iCurrent = simple_force_assignment.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent    

    iCurrent = simple_release_assignment.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent    

#    iCurrent = simple_waveform_assignment.detect(iToken, lObjects)

    return iCurrent
