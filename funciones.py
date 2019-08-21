#****************************************************************
#*************************ejercicios de python*******************
#****************************************************************
import math

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
    a=[]
    for i in range(a):
        a.append(i)
    for i in range(a -1):
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

def prob_8(j):
    i=1
    while i<=j:
        print((j*' ')+i*'* ')
        j=j-1
        i=i+1


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
def Prob_10(ax1, ay2, bx1, by2, cx1, cy2):
    r1 = math.sqrt((ax1*bx1)**2+(ay2*by2)**2)
    r2 = math.sqrt((bx1*cx1)**2+(by2*cy2)**2)
    r3 = math.sqrt((cx1*ax1)**2+(cy2*ay2)**2)
    print (r1, r2, r3)
    if r1>r2>r3:
        r2+r3 ==r1
        return True
    elif r1>r3>r2:
        r3+r2==r1
        return True
    elif r1<r2<r3:
        r1+r2==r3
        return True
    elif r2<r1<r3:
        r2+r1==r3
        return True
    elif r2>r1>r3:
        r1+r3==r2
        return True
    elif r2>r3>r1:
        r3+r1==r2
        return True
    else:
        return False
    

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
#Espacio para trabajar en la funcion
#prob_13():


#verificacion si un numero es primo

def prob_14(numero):
    if numero <= 1:
        return ("ingrese un numero mayo a 1")
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
        if (n % (i) == 0):
            suma += (i)
    if n==suma:
        return True
    else:
        return False

#Verificacion de que sean Numero amigos
#Espacio para trabajar la funcion
#pob_16():


#veridicacion de ue sean Primos Relativos

def prob_17(n1, n2):
    suma=0
    if n1 and n2 <= 1:
        return ("el numero debe de ser mayo a 1")
    else:
        contador1 = 0
        contador2 = 0
        for i in range(1, n1 + 1):
            if n1 % i == 0:
                contador1 = contador1 + 1
        for i in range(1, n2 + 1):
            if n2 % i == 0:
                contador2 = contador2 + 1
        if contador2 == 2:
            return True
        else:
            return ("Uno de los dos o los dos no son primos")

#serie de numero fibonacci

def prob_18(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    return n
        
#cumple con tener ese ese mismo numero de digitos

def prob_19(n):
    a, b = 0,1
    while a < n:
        a,b = b, a+b
    return True

#Encuentra las tripletas pitagoricas

def prob_20(a, b, c):
    total = 1000
    if a**2+b**2+c**2 == total:
        return("es una tripleta pitagorica")
    else:
        return ("No es una tripleta pictagorica")
