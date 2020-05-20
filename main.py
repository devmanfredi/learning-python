my_var = 2
my_var = 'dois'
my_var = 2.0
my_var = int(my_var)

x = 1
y = 4.3
z = x + y
print(type(x))
print(type(y))
print(type(z))

x = 1
z = 2
print("x/z = " + str(x/z)) 
print("x//z = " + str(x//z))

nota_1 = 5
nota_2 = 3
print(nota_1+nota_2)

nota_1 = str(5)
nota_2 = str(3)
nota_3 = nota_1 + nota_2
print(nota_3)

#---------
x = 2
y = 3.0
z = 8
print(x != 7)
print(x > y)
print((y//x) ==1)
print((y/x) ==1)
print((x**2) == 4)
print(z == 9 or z < 9)
print(z < 9 or z == 9)
print(x == 2 and z == x)

#--------
idade = 18
if idade >= 18:
  print("Pode dirigir")
else :
  print("Não pode drigir")

#---------
turno = input("Digite o seu turno \n")
if(turno == "M"):
  print("Bom dia")
elif (turno == "V"):
  print("Boa tarde")
elif (turno == "N"):
  print("Noturno")
else :
  print("Valor inválido")

#------------------
i = 1
while( i <= 20):
  print(i)
  i = i + 1

#------------------
numeros = [1,2,3,4,5,6,7,8,9,10]
n_tabuada = int(input("digite a tabuada que deseja encontrar :  "))
for numero in numeros:
  print(str(n_tabuada) + " X " + str(numero) + " = " + str(numero * n_tabuada))