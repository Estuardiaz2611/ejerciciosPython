#****************************************************************
#*************************ejercicios de python*******************
#****************************************************************

from math import sqrt, floor

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

def prob_4(msj,size):
    return msj.center(size,"*")

#funcion de cruz

def prob_5(nA1, nB1, nC1, nA2, nB2, nC2):
      resultado1 = ((nB1*nC2)-(nB2*nC1))
      resultado2 = -((nA1*nC2)-(nA2*nC1))
      resultado3 = ((nA1*nB2)-(nA2*nB1))
      return resultado1, resultado2, resultado3

#bubble sort descendente

def prob_6(a):
    n = len(a)
    for i in range(n):
        for j in range(n -1):
            if(a[j]<a[j+1]):
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

def prob_8(n):
    piramide = ""
    if n == 0:
        return None
    elif n == 1:
        return "*"
    else:
        for i in range(n-1, 0, -1):
            es = " " * i
            asteriscos = "* " * (n-i)
            piramide += es + asteriscos + "\n"

    return piramide

#tripletas pitagoricas problema 9

def prob_9(c1, c2, c3):
    if c1>c2>c3:
        p1 = c2**2+c3**2
        p2 = c1**2
        r1 = p1==p2
        return True
    elif c1>c3>c2:
        p1 = c2**2+c3**2
        p2 = c1**2
        r1 = p1==p2
        return True
    elif c1<c2<c3:
        p3 = c1**2+c2**2
        p4 = c3**2
        r2 = p3==p4
        return True
    elif c2<c1<c3:
        p3 = c1**2+c2**2
        p4 = c3**2
        r2 = p3==p4
        return True
    elif c2>c1>c3:
        p4 = c1**2+c3**2
        p5 = c2**2
        r3 = p4==p5
        return True
    elif c2>c3>c1:
        p4 = c1**2+c3**2
        p5 = c2**2
        r3 = p4==p5
        return True
    else:
        return False

#Treingulo con puntos
def prob_10(a,b,c):
    r1 = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    r2 = sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    r3 = sqrt((c[0] - a[0])**2 + (c[1] - a[1])**2)
    total = [r1, r2, r3]
    if total[0] + total[1] <= total[2]:
        return ("no es un triangulo")
    if total[0]==total[1] and total[1]==total[2]:
        return ("Triangulo Equilatero")
    elif total[0]==total[1] or total[1] == total[2]:
        return ("Triangulo Isosceles")
    else:
        return ("Triangulo Escaleno")



#invertir palabras

def prob_11(msj):
    cadenaInvertida = msj[::-1]
    if msj==cadenaInvertida:
        return True
    else:
        return False

#convertir de numero a letras

def prob_12(n):
    lista=list(str(n))
    inverse,new,con,=lista[::-1],['','','','','','','','',''],0
    for i in inverse:
        new[con]=int(i)
        con+=1
    a,b,c,d,e,f,g,h,i=new[::-1]
    if len(str(new[3]))>0:
        new.insert(3,'.')
    if len(str(new[7]))>0:
        new.insert(7,'.')
    numero=new[::-1]
    if n>1000:
        return ("fuera de rango ingrese numero entre 1 y 1000")
    for i in numero:
        print(str(i),end='')
    print()    
    unidad={1:'un', 2:'dos', 3:'tres', 4:'cuatro', 5:'cinco', 6:'seis', 7:'siete', 8:'ocho', 9:'nueve',0:'','':''}
    unidadi={1:'uno', 2:'dos', 3:'tres', 4:'cuatro', 5:'cinco', 6:'seis', 7:'siete', 8:'ocho', 9:'nueve',0:'','':''}
    unidad2={10:'diez', 11:'once', 12:'doce', 13:'trece', 14:'catorce', 15:'quince',16:'diez y seis',17:'diez y siete', 18:'diez y ocho', 19:'diez y nueve'}
    decena={1:'diez', 2:'veinti', 3:'treinta', 4:'cuarenta', 5:'cincuenta', 6:'sesenta', 7:'setenta', 8:'ochenta', 9:'noventa','':'',0:''}
    centena={1:'ciento', 2:'dos cientos',3:'tres cientos',4:'cuatro cientos',5:'quinientos',6:'seis cientos',7:'setecientos',8:'ocho cientos',9:'novecientos','':'',0:''}
    
    d=centena[d]
    if e==1 and f<6:
        e,f=unidad2[int(str(e)+str(f))],'mil'
    elif f==0:
        e,f=decena[e],'mil'
    elif e==0:
        e,f='',(unidad[f]+len(str(f))*' mil')
    else:
        e=(decena[e]+len(str(e))*' y')
        f=(unidad[f]+len(str(f))*' mil')
    g=centena[g]
    if h==1 and i<6:
        h,i=unidad2[int(str(h)+str(i))],''
    elif h==0:
        h,i='',unidadi[i]
    else:
        if i==0:
            i,h='',decena[h]
        else:
            i,h=unidadi[i],decena[h]+len(str(h))*' y'
    orden=[a,b,c,d,e,f,g,h,i]
    return orden

#suma de divisores de un numero

def prob_13(numero):
    resultado = 0
    for i in [1, numero]:
        if numero%i == 0:
            resultado += i
    return resultado


#verificacion si un numero es primo

def prob_14(numero):
    if numero <= 1:
        return ("ingrese un numero mayor a 1")
    else:
        contador = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                contador = contador + 1
        if contador == 2:
            return True
        else:
            return False

#Verificacion de numeros perfectos

def prob_15(n):
    suma=0
    for i in range(1,n):
        if (n%i == 0):
            suma += (i)
    if n==suma:
        return True
    else:
        return False

#Verificacion de que sean Numero amigos

def prob_16(n1, n2):
    tX = 0
    tR = 0
    for i in range(1, n1):
        if n1%i == 0:
            tX += i
        if n2%i == 0:
            tR += i

    return tX == n2 and tR == n1


#veridicacion de ue sean Primos Relativos

def prob_17(n1, n2):
    ar = []
    for i in range(2, n1):
        if n1%i == 0:
            ar.append(i)

    for i in range(2, n2):
        if n2%i == 0 and i in ar:
            return False

    return True

#serie de numero fibonacci

def prob_18(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    return n
        
#cumple con tener ese ese mismo numero de digitos

def prob_19(n):
    x = 0
    y = 1
    while True:
        if len(str(x)) == n:
            return x
        x, y = y, x+y


#Encuentra las tripletas pitagoricas

def prob_20():
    ar = []
    for j in range(1, 1000):
        for i in range(j+1, 1000):
            a = i**2 - j**2
            b = 2*j*i
            c = j**2 + i**2
            if ((a**2 + b**2) == c**2) and (a + b + c) == 1000:
                ar.append([a,b,c])

    return ("Los valores son: ", ar)

#Dado un entero positivo, encontrar todos los nuemeros primos

def prob_21(n):
    almacenar = []
    for i in range(2, n+1):
        if prob_14(i):
            almacenar.append(i)
    return almacenar

#Encontrar si es cuadrado

def prob_22(pts1, pts2, pts3, pts4):
    if pts1 == pts2:
        return False
    elif pts2 == pts3:
        return False
    elif pts3 == pts4:
        return False
    else:
        distancia1 = sqrt((pts1[0] - pts2[0])**2 + (pts1[1] - pts2[1])**2)
        distancia2 = sqrt((pts1[0] - pts3[0])**2 + (pts1[1] - pts3[1])**2)
        distancia3 = sqrt((pts1[0] - pts4[0])**2 + (pts1[1] - pts4[1])**2)
        r1 = [distancia1,distancia2,distancia3]
        distancia4 = sqrt((pts4[0] - pts1[0])**2 + (pts4[1] - pts1[1])**2)
        distancia5 = sqrt((pts4[0] - pts2[0])**2 + (pts4[1] - pts2[1])**2)
        distancia6 = sqrt((pts4[0] - pts3[0])**2 + (pts4[1] - pts3[1])**2)
        r2 = [distancia4, distancia5, distancia6] 
        return r1 == r2

#dada una lista, encuentre una lista con todas las posibles listas

def prob_24(numeros):
    orden = numeros
    numerosOrdenados = [orden.copy()]
    ref = []
    n = len(orden)

    for i in range(n):
        ref.append(0)

    i = 0

    while i < n:
        if ref[i] < i:
            if prob_1(i):
                orden[0], orden[i]= orden[i], orden[0]
            else:
                orden[ref[i]], orden[i] = orden[i], orden[ref[i]]
            numerosOrdenados.append(orden.copy())
            ref[i] += 1

            i = 0
        else:
            ref[i] = 0
            i += 1

    return numerosOrdenados
