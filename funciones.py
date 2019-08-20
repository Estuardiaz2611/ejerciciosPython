#funcion par impar 

def prob_1(n):
    if n%2==0:
        return True
    else:
        return False


#funcion de conversion
    
def prob_2(n):
   return ((n - 32)*5/9)

#funcion de potencia

def prob_3(base, potencia):
      return base**potencia

#funcion de parrafo

def prob_4(message,size):
    return message.center(size,"*")

#funcion de cruz

def prob_5(nA1, nB1, nC1, nA2, nB2, nC2):
      resultado1 = ((nB1*nC2)-(nB2*nC1))
      resultado2 = -((nA1*nC2)-(nA2*nC1))
      resultado3 = ((nA1*nB2)-(nA2*nB1))
      return resultado1, resultado2, resultado3

#bubble sort descendente

def prob_6(n):
    a=[]
    for i in range(n):
        value=int(input("ingrese los elementos: " %i))
        a.append(value)
    for i in range(n -1):
        if(a[j]>a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
    return (a)

#Multiplos

def prob_7(n, m):
    i=0
    multiplo = []
    while i<=n:
        if i % m == 0:
            multiplo.append(i)
            i=i+1
        else:
            i= i+1
    return multiplo
        



#piramide de asteriscos Problema 8

def prob_8():
    i=1
    j=5
    while i<=5:
        print((j*' ')+i*'* ')
        j=j-1
        i=i+1


#tripletas pitagoricas problema 9

"""def prob_9(c1, c2, c3):
      


if es_rectangulo(c1, c2, c3):
      # cualuier cosa sabiendo ue es rectangulo



def pitagoras():
      
valor = pitagoras()
print (valor)
"""
