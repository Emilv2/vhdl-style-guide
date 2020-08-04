
from vsg.token import interface_signal_declaration as token
from vsg import parser

lModes = ['in', 'out', 'inout', 'buffer', 'linkage']


def interface_signal_declaration(oObject, iObject, lObjects, dVars):
    '''
    Classifies signal interface declarations:

    [ signal ] identifier_list : [ mode ] subtype_indication [ bus ] [ := static_expression ] ;

    '''
    if not dVars['bInterfaceSignalDeclarationColonFound']:
        if classify_keyword(oObject, iObject, lObjects, dVars):
            return
        classify_comma(oObject, iObject, lObjects, dVars)
        classify_identifier(oObject, iObject, lObjects, dVars)
        classify_colon(oObject, iObject, lObjects, dVars)
    else:
        if not dVars['bInterfaceSignalDeclarationAssignmentOperatorFound']:
            if classify_assignment_operator(oObject, iObject, lObjects, dVars):
                return
            classify_subtype_indication(oObject, iObject, lObjects, dVars)
            classify_mode_keyword(oObject, iObject, lObjects, dVars)
            classify_bus_keyword(oObject, iObject, lObjects, dVars)
        else:
            classify_static_expression(oObject, iObject, lObjects, dVars)
            


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'signal':
        lObjects[iObject] = token.keyword(sValue)
        return True
    return False


def classify_identifier(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item and sValue != ',' and sValue != '(' and sValue != ';':
        lObjects[iObject] = token.identifier(sValue)


def classify_comma(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ',':
        lObjects[iObject] = token.comma()


def classify_colon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':':
        lObjects[iObject] = token.colon()
        dVars['bInterfaceSignalDeclarationColonFound'] = True


def classify_mode_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() in lModes:
        lObjects[iObject] = token.mode_keyword(sValue)


def classify_subtype_indication(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item and sValue.lower() != 'bus' and sValue.lower() not in lModes and sValue != ';':
        lObjects[iObject] = token.subtype_indication(sValue)


def classify_bus_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'bus':
        lObjects[iObject] = token.bus_keyword(sValue)


def classify_assignment_operator(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':=':
        lObjects[iObject] = token.assignment_operator(':=')
        dVars['bInterfaceSignalDeclarationAssignmentOperatorFound'] = True
        return True
    return False


def classify_static_expression(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item and sValue.lower() != ':=':
        lObjects[iObject] = token.static_expression(sValue)


def clear_flags(dVars):
    dVars['bInterfaceSignalDeclarationAssignmentOperatorFound'] = False
    dVars['bInterfaceSignalDeclarationColonFound'] = False
