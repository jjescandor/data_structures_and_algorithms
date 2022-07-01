from stack import Stack


def multi_bracket_validation(brackets):
    bracketcont, type = Stack(), {"(": ")", "{": "}", "[": "]"}
    for bracket in brackets:
        if bracket in type.keys():
            bracketcont.push(bracket)
        if bracket in type.values() and type[bracketcont.pop()] == bracket:
            return False
    return bracketcont.is_empty()


def multi_bracket_validation_(brackets):
    bracketcont, type = [], {"(": ")", "{": "}", "[": "]"}
    for bracket in brackets:
        if bracket in type.keys():
            bracketcont.append(bracket)
        if bracket in type.values() and type[bracketcont[-1]] != bracket:
            return False
    return len(bracketcont) == 0


def multi_bracket_validation_(brackets):
    round = 0
    curly = 0
    square = 0
    close = None
    for bracket in brackets:
        if bracket == "{":
            close = False
            curly += 1
        if bracket == "}":
            close = True
            curly -= 1
        if bracket == "(":
            close = False
            round += 1
        if bracket == ")":
            close = True
            round -= 1
        if bracket == "[":
            close = False
            square += 1
        if bracket == "]":
            close = True
            square -= 1
    if not close:
        return False
    if round == 0 and curly == 0 and square == 0:
        return True
    else:
        return False


def multi_bracket_validation(brackets):
    bracketcont = []
    type = {"(": ")", "{": "}", "[": "]"}
    for bracket in brackets:
        if bracket in type.keys():
            bracketcont.append(bracket)
        if bracket in type.values():
            if len(bracketcont) == 0:
                return False
            if type[bracketcont[-1]] == bracket:
                bracketcont.pop()
    return len(bracketcont) == 0
