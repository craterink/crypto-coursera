

# enum pattern
class UnknownPTLetterW1:

    SPACE, LOWER, UPPER, ELSE = range(4)

    # tuple of unknown letter possibilities
    _possibilities = ()

    def __init__(self):
        self._possibilities = {
            self.SPACE : True,
            self.LOWER : True,
            self.UPPER : True,
            self.ELSE : True
        }

    def _set_poss(self, poss, val):
        self._possibilities[poss] = val

    def rule_out(self, ltr_poss):
        self._set_poss(ltr_poss, False)

    def rule_in(self, ltr_poss):
        self._set_poss(ltr_poss, True)