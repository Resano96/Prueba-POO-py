class Cafe():
    def que_soy(self):
        print("Soy un cafe")

class Te():
    def que_soy(self):
        print("Soy un te")

def definicion_bebida(bebida):
    bebida.que_soy()

definicion_bebida(Te())