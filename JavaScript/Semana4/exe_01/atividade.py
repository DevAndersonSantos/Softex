class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def add(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return ComplexNumber(real_part, imag_part)

    def subtract(self, other):
        real_part = self.real - other.real
        imag_part = self.imag - other.imag
        return ComplexNumber(real_part, imag_part)

    def multiply(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return ComplexNumber(real_part, imag_part)

    def divide(self, other):
        denominator = (other.real ** 2) + (other.imag ** 2)
        real_part = ((self.real * other.real) + (self.imag * other.imag)) / denominator
        imag_part = ((self.imag * other.real) - (self.real * other.imag)) / denominator
        return ComplexNumber(real_part, imag_part)

# Exemplo de uso:
num1 = ComplexNumber(3, 2)
num2 = ComplexNumber(1, 4)

# Operações básicas
soma = num1.add(num2)
subtracao = num1.subtract(num2)
multiplicacao = num1.multiply(num2)
divisao = num1.divide(num2)

# Imprimindo propriedades real e imag
print(f"Número 1: {num1.real} + {num1.imag}i")
print(f"Número 2: {num2.real} + {num2.imag}i")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
