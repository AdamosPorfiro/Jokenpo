class Sistema:
    def __init__(self):
        self.estado = None

    def definir_estado(self):
        self.estado = "ativo"

    def verificar_estado(self):
        if self.estado == "ativo":
            print("O estado está ativo!")
        else:
            print("O estado não está ativo.")

sistema = Sistema()
sistema.definir_estado()
sistema.verificar_estado()
