from mmap import mmap
import numpy as np    
import matplotlib.pyplot as plt   

#datos 
#n= número de elementos  

f1=30000          #valores del problema
f2=40000
n=int(input("Ingresar cuantos elementos cilindricos"))
j=1             #valores dados para el bucle
e=30
while j<n:   #generar un bucle 
    j+=1     # se suman asi mismos
    e+=e
Fi=0         #inicializar la siguiente while
i=1
F=0
d=10
while i<=n and d<=e:       #se pone dos condiciones
    F=Fi+f1                #ecuaciones para sacar el esfuerzo 
    A=np.pi*d**2/4
    E=round(F/A,2)
    print("ESFUERZO {0}".format(i),"=",E)  #el metodo format da el formato y resultado de esfuerzo y area de cada elemento cilindrico
    print("AREA {0}".format(i),"=",A)
    i+=1
    d+=20                                  #se suman asi mismos los valores dados
    Fi+=f2
print("Gracias por participar")
    
