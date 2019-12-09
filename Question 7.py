def signFinder (s):
    plus = s.count("-")
    minus = s.count("+")
    total = plus+minus
    if total == 1:
        return True
    else:
        return False