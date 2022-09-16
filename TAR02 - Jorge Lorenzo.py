#Escribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada de la suma del cuadrado de ambos.
#Jorge Lorenzo (JL21-1895), 9/16/22.
#Este es el link del repositorio en Github: https://github.com/JorgelRight34/TECNICASDEPROGRAMACION.git
#Seccion para la declaracion de num1 y num2.
import math
num1 = round(float(input("Ingrese un numero")))
num2 = round(float(input("Ingrese un numero")))

#Estas son las operaciones matematicas a utilizar.
num1_square = (num1**2)
num2_square = (num2**2)
addition_result = num1_square + num2_square
entire_calculation = math.sqrt(num1_square + num2_square)

#Estos son los elementos forman parte de lo que sera imprimido en los prints.
firstprint =  "√(" + str(num1) + "²" " + " + str(num2) + "²" + ")"
secondprint = "√(" + str(num1_square) + " + " + str(num2_square) + ")"
thirdprint = "√(" + str(addition_result) + ")"
fourtprint = "√(" + str(addition_result) + ")"

print(firstprint + " = " + secondprint + " = " + fourtprint + " = " + str(entire_calculation))
