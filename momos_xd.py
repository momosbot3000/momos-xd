import random

myN = 1
lose = 0
win = 0
tie = 0

def nString(case):
    if case == 1:
       return "Piedra"
    elif case == 2:
        return "Papel"
    elif case == 3:
        return "Tijera"

def system(a, b):

    if(a == b):
        return 0
    elif a == 1:
        return - (a - (b - 2) * 2)
    elif a == 2:
        return a - b
    elif a == 3:
        return - ((a - 2) - (b - 1) * 2)
            
def sString(case):
    if case == -1:
        return "Ronda Perdida"
    elif case == 0:
        return "Empate"
    elif case == 1:
        return "Ronda Ganada"


print("Piedra papel o tijeras\n")
print("Reglas: cada numero tiene un objeto asignado, 1 para piedra, 2 para papel y 3 para tijeras \n"
      "Presione 0 para terminar y ver puntuacion")

while myN != 0:

    myN = int(input('Introdusca un valor 1 al 3: '))

    while not(myN >= 0 and myN <= 3):
        myN = int(input('Introdusca un valor valido: '))
        
    n = random.randint(1,3)
    sn = nString(n)
    smyN = nString(myN)
    if(myN != 0):
        print("\n", smyN, " vs ", sn)
        count = system(myN, n);

    if count == -1:
        lose += 1
    elif count == 0:
        tie += 1
    elif count == 1:
        win += 1
    print(sString(count), "\n")

print(' Ganadas : ', win,"\n",
      'Perdidas : ', lose, "\n",
      'Empate : ',  tie, "\n")