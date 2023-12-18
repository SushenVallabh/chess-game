def rook(t1, t2):
    if t1 == t2:
        return True
    if t1[0] == t2[0] or t1[1] == t2[1]:
        return True
    return False


def bishop(t1, t2):
    if t1 == t2:
        return True
    if abs(t1[0] - t2[0]) == abs(t1[1] - t2[1]):
        return True
    return False


def knight(t1, t2):
    if t1 == t2:
        return True
    if abs(t1[0] - t2[0]) == 200:
        if abs(t1[1] - t2[1]) == 100:
            return True
        else:
            return False
    elif abs(t1[1] - t2[1]) == 200:
        if abs(t1[0] - t2[0]) == 100:
            return True
        else:
            return False
    else:
        return False


def queen(t1, t2):
    if (abs(t1[0] - t2[0]) == abs(t1[1] - t2[1])) or (t1[0] == t2[0] or t1[1] == t2[1]):
        return True
    if t1 == t2:
        return True
    return False


def king(t1, t2):
    if abs(t1[0]-t2[0]) <= 100 and abs(t1[1]-t2[1]) <= 100:
        return True
    return False


def black_pawn(t1, t2, item):

    if item is not None:
        if abs(t1[0]-t2[0]) == 100 and t2[1] == t1[1] + 100:
            return True
        else:
            return False
    else:
        if t1[0] == t2[0] and t1[1] == 100 and t2[1] == 300:
            return True
        elif t1[0] == t2[0] and t2[1] == t1[1] + 100:
            return True
        else:
            return False


def white_pawn(t1 ,t2, item):
    if item is not None:
        if abs(t1[0] - t2[0]) == 100 and t2[1] == t1[1] - 100:
            return True
        else:
            return False
    else:
        if t1[0] == t2[0] and t1[1] == 600 and t2[1] == 400:
            return True
        elif t1[0] == t2[0] and t2[1] == t1[1] - 100:
            return True
        else:
            return False


piece_path = {'king': king, 'queen': queen, 'rook': rook, 'knight': knight, 'bishop': bishop}

