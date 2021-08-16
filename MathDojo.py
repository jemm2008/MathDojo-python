class MathDojo:
    def __init__(self):
        self.resultado = 0

    def add(self, num, *nums):
        self.resultado += num
        for item in nums:
            self.resultado += item
        print("salida add ", self.resultado)
        return self

    def subtract(self, num, *nums):
        self.resultado -= num
        for item in nums:
            self.resultado -= item
        print("salida sub ", self.resultado)
        return self

md=MathDojo()

################################################################
#x = md.add(2,5,1).subtract(3,2).resultado
print("PRUEBA FINAL...\n")

x = md.add(2).add(2,5,1).subtract(3,2).resultado
print("\n'x' es igual a ", x)	# debe imprimir 5