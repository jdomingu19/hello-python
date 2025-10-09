print("ACTIVIDAD CALCULADORA DE FRACCIONARIOS - ALGORITMOS I_CORTE 2 - JOSÉ MARTÍNEZ")

print("")

print("EJERCICIOS")

print("")

print("-Método sumar (Homogénea y heterogénea)")
print("-Método restar")
print("-Método multiplicar")

print("")

print("---------------------------------------")

print("")

class fraccionario:
    def __init__(self):

        self.numerador=0
        self.denominador=0
        
    def setNumerador(self,x:int):
        self.numerador=x
        
    def getNumerador(self):
        return self.numerador

    def setDenominador(self,x:int):
        self.denominador=x
        
    def getDenominador(self):
        return self.denominador
    
class calculadoraFracciones:
    def __init__(self):
        self.f1=fraccionario()
        self.f2=fraccionario()

    def setF1(self,x:fraccionario()):
        self.f1=x

    def getF1(self):
        return self.f1

    def setF2(self,x:fraccionario()):
        self.f2=x

    def getF2(self):
       return self.f2

    def fraccionesheterogenea(self):
        numerador=(self.f1.getNumerador()*self.f2.getDenominador())+(self.f1.getDenominador()*self.f2.getNumerador())
        denominador=self.f1.getDenominador()*self.f2.getDenominador()
        print(f"Suma heterogénea {numerador} / {denominador} = {numerador / denominador}")

    def Fraccioneshomogeneas(self):
        numerador=(self.f1.getNumerador()+self.f2.getNumerador())
        denominador=self.f1.getDenominador()
        print(f"Suma homogénea {numerador} / {denominador} = {numerador / denominador}")
        
    def restaFracciones(self):
        numerador=(self.f1.getNumerador()*self.f2.getDenominador())-(self.f1.getDenominador()*self.f2.getNumerador())
        denominador=self.f1.getDenominador()*self.f2.getDenominador()
        print(f"Resultado de la resta {numerador} / {denominador} = {numerador / denominador}")
        
    def multiFracciones(self):
        numerador=(self.f1.getNumerador()*self.f2.getNumerador())
        denominador=(self.f1.getDenominador()*self.f2.getDenominador())
        print(f"Resultado de la multiplicación {numerador} / {denominador} = {numerador / denominador}")
        
def main():
    f1=fraccionario()
    f1.setNumerador(10)
    f1.setDenominador(20)
    
    f2=fraccionario()
    f2.setNumerador(30)
    f2.setDenominador(40)

    print(f"Fracción 1: {f1.getNumerador()} / {f1.getDenominador()}")
    print(f"Fracción 2: {f2.getNumerador()} / {f2.getDenominador()}")

    print("")

    #Suma_Heterogenea(++++)
    calc1=calculadoraFracciones()

    calc1.setF1(f1)
    calc1.setF2(f2)
    calc1.fraccionesheterogenea()

    #Resta(----)
    calc1.setF1(f1)
    calc1.setF2(f2)
    calc1.restaFracciones()
    
    #Multiplicacion(****)
    calc1.setF1(f1)
    calc1.setF2(f2)
    calc1.multiFracciones()

    print("")

    #####################################
    print("¡¡.....!!")

    print("")

    #Suma_homogenea(++++)
    f1=fraccionario()
    f1.setNumerador(5)
    f1.setDenominador(8)

    f2=fraccionario()
    f2.setNumerador(7)
    f2.setDenominador(8)
    
    print(f"Fracción 1: {f1.getNumerador()} / {f1.getDenominador()}")
    print(f"Fracción 2: {f2.getNumerador()} / {f2.getDenominador()}")

    print("")
    
    calc1.setF1(f1)
    calc1.setF2(f2)
    calc1.Fraccioneshomogeneas()
        
main()    