
from vsg.token import port_clause as token

from vsg.vhdlFile.classify import interface_list


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    Classifies the beginning portion of port clauses:

        port ( port_list ) ;

    '''
    if not dVars['bPortClauseKeywordFound']:
        classify_keyword(oObject, iObject, lObjects, dVars)
    else:
        if not dVars['bPortClauseOpenParenthesisFound']:
            classify_open_parenthesis(oObject, iObject, lObjects, dVars)
        else:
            if not dVars['bPortClauseCloseParenthesisFound']:
                if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
                    interface_list.clear_flags(dVars)
                    return True
                interface_list.interface_list(oObject, iObject, lObjects, dVars)
            else:
                classify_semicolon(oObject, iObject, lObjects, dVars)


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'port':
        lObjects[iObject] = token.keyword(sValue)
        dVars['bPortClauseKeywordFound'] = True


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == '(':
        lObjects[iObject] = token.open_parenthesis()
        dVars['bPortClauseOpenParenthesisFound'] = True
        dVars['iOpenParenthesisCount'] = 1
        dVars['iCloseParenthesisCount'] = 0


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ')':
        dVars['iCloseParenthesisCount'] += 1
        if dVars['iOpenParenthesisCount'] == dVars['iCloseParenthesisCount']:        
            dVars['bPortClauseCloseParenthesisFound'] = True
            lObjects[iObject] = token.close_parenthesis()
            return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        dVars['bPortClauseKeywordFound'] = False
        dVars['bPortClauseOpenParenthesisFound'] = False
        dVars['bPortClauseCloseParenthesisFound'] = False