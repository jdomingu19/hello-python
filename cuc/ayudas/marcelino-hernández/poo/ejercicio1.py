# Ejercicio 1

class Cuenta():
    def __init__(self, numero, tipo, saldo_actual):
        self.__numero = numero
        self.__tipo = tipo
        self.__saldo_actual = saldo_actual
        self.__saldo_minimo = saldo_actual * 0.15

    def set_numero(self, numero):
        self.__numero = numero

    def get_numero(self):
        return self.__numero

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def set_saldo_actual(self, saldo_actual):
        self.__saldo_actual = saldo_actual

    def get_saldo_actual(self):
        return self.__saldo_actual

    def set_saldo_minimo(self, saldo_minimo):
        self.__saldo_minimo = saldo_minimo

    def get_saldo_minimo(self):
        return self.__saldo_minimo

    def consignar(self):
        valor_consignacion = eval(input("Ingrese valor a consignar: $"))
        self.set_saldo_actual((self.set_saldo_actual() + valor_consignacion))
    
    def retirar(self):
        if self.get_tipo() == "ahorro":
            valor_retirar = eval(input("Ingrese valor a retirar: $"))

            while self.get_saldo_actual() - valor_retirar < self.get_saldo_minimo():
                print("No puede sobrepasar el saldo mínimo...")
                print(f"Máximo territo: {self.get_saldo_actual() - self.get_saldo_minimo()}")

            self.set_saldo_actual((self.set_saldo_actual() - valor_retirar))
        else:
            valor_retirar = eval(input("Ingrese valor a retirar: $"))

            while self.get_saldo_actual() - valor_retirar < 0:
                print("No puede retirar más de lo que tiene...")
                print(f"Máximo territo: {self.get_saldo_actual()}")

            self.set_saldo_actual((self.set_saldo_actual() - valor_retirar))

def main():
    print("CUENTA 1")
    cuenta1 = Cuenta(123, "ahorro", 1000000)
    cuenta1.consignar()
    cuenta1.retirar()

    print("")

    print("CUENTA 2")
    cuenta1 = Cuenta(345, "crédito", 2000000)
    cuenta1.consignar()
    cuenta1.retirar()
main()