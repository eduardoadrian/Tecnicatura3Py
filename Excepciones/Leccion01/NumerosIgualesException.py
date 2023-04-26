class NumerosIgualesException (Exception): # Extiende dela clase
    def __init__(self, mensaje):
        self.message = mensaje
