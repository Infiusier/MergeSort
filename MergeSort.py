#MERGESORT
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import sys
sys.setrecursionlimit(10**9)
lista=[]
tamanhos=[20000,40000,60000,80000,100000]
tempos=[]
def geraLista(tamanho):
  x=[]
  for i in range(tamanho): x.append(i)
  random.shuffle(x)
  return x

def geraListaPiorCaso(tamanho):
  x=[]
  for i in range(tamanho,0,-1):
    x.append(i)
  return x

def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista)//2
        left = lista[:mid]
        right = lista[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              lista[k] = left[i]
              i += 1
            else:
                lista[k] = lista[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k]=right[j]
            j += 1
            k += 1

for i in tamanhos:
  print("comecei")
  lista=geraLista(i)
  
  #lista=geraListaPiorCaso(i)
  print("terminei")
  now=time.time()
  print("comecei dnv")
  mergeSort(lista)
  print("acabei dnv")
  then=time.time()
  tempos.append(then-now)
# Plot the data
plt.plot(tamanhos,tempos)
print(tempos)
# Show the plot
plt.show()
