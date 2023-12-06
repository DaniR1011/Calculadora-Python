# EJERCICIO CALCULADORA EN PYTHON

# Realizamos las operaciones matemáticas
def sumar(x, y):
 return x + y

def restar(x, y):
 return x - y

def multiplicar(x, y):
 return x * y

def dividir(x, y):
 if y != 0:
  return x / y
 else:
  return 'MATH OPERATION ERROR'

def potencia(x, y):
 return x ** y

def raiz_cuadrada(x):
 if x >= 0:
  return x ** 0.5
 else:
  return 'MATH OPERATION ERROR'

# Definimos la estructura principal de nuestra calculadora
def calculadora():
 print("¡Bienvenido a la Calculadora!")
 while True:
  operación_a_realizar = input('Selecciona una operación: Sumar(1) / Restar(2) / Multiplicar (3) / Dividir (4) / Elevar un número a otro (5) / Raíz Cuadrada (6) / Salir (7) : ')
  if operación_a_realizar == '7':
   print('¡Espero que hayas solucionado tu duda! 😊')
   break
  
  elif operación_a_realizar in ['1','2','3','4','5']:
   x = int(input('Introduce el primer número: '))
   y = int(input('Introduce el segundo número: '))
   if operación_a_realizar == '1':
    result = sumar(x,y)
   if operación_a_realizar == '2':
    result = restar(x,y)
   if operación_a_realizar == '3':
    result = multiplicar(x,y)
   if operación_a_realizar == '4':
    result = dividir(x,y)
   if operación_a_realizar == '5':
    result = potencia(x,y)
   
  elif operación_a_realizar == '6':
   x = int(input('Introduce el número sobre el que realizar la raíz cuadrada: '))
   result = raiz_cuadrada(x)

  else:
   print(f'{operación_a_realizar} No es una opción válida')
   result = False
  if result:
   print(result)

if __name__ == "__main__":
 calculadora()

