class NotAllowed(Exception):
    pass

class BadAcc(Exception):
    def __str__(self):
        return "Mauvais compte"

class BadOperation(Exception):
    def __str__(self):
        return "Mauvaise Opération"