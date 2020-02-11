import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','generate','generate_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testVhdlFileGenerateAssignments(unittest.TestCase):


    def test_isGenerateKeyword(self):
        lExpected = [6,11,16,21,26,31,36,41,46,51,56,60,65,68,71,77,83,88,90,94,105,110]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenerateBegin(self):
        lExpected = [7,12,17,22,27,32,37,42,47,52,84]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateBegin:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenerateEnd(self):
        lExpected = [9,14,19,24,29,34,39,44,49,54,58,62,73,75,79,81,86,96,98,100,106,112]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndArchitecture(self):
        lExpected = [114]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_GenerateIndent(self):
        #           [   0,   1,2,   3,4,   5,6,7,8,9,  10,11,12,13,14,  15]
        lExpected = [None,None,0,None,0,None,1,1,2,1,None, 1, 1, 2, 1,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideGenerate(self):
        lExpected = [6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24,26,27,28,29,31,32,33,34,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,56,57,58,60,61,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,85,86]
        lExpected.extend(range(88, 101))
        lExpected.extend(range(104, 107))
        lExpected.extend(range(110, 113))
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideGenerate:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isGenerateLabel(self):
        lExpected = [6,11,16,21,26,31,36,41,46,51,56,60,65,68,71,77,83,88,90,94,104,110]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isGenerateLabel:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
