import random
import time

dados = [random.randint(1, 100000) for _ in range(5000)]

def bubble_sort(arr):
    n = len(arr)
    tempo_inicio = time.time()
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    tempo_fim = time.time()
    return arr, tempo_fim - tempo_inicio

def selection_sort(arr):
    tempo_inicio = time.time()
    for i in range(len(arr)):
        indice_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[indice_min]:
                indice_min = j
        arr[i], arr[indice_min] = arr[indice_min], arr[i]
    tempo_fim = time.time()
    return arr, tempo_fim - tempo_inicio

def insertion_sort(arr):
    tempo_inicio = time.time()
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i-1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    tempo_fim = time.time()
    return arr, tempo_fim - tempo_inicio

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        L = arr[:meio]
        R = arr[meio:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

ordenado_bubble, tempo_bubble = bubble_sort(dados.copy())
ordenado_selection, tempo_selection = selection_sort(dados.copy())
ordenado_insertion, tempo_insertion = insertion_sort(dados.copy())
ordenado_merge = merge_sort(dados.copy())

print("Bubble Sort: Ordenado:", ordenado_bubble, "Tempo:", tempo_bubble)
print("Selection Sort: Ordenado:", ordenado_selection, "Tempo:", tempo_selection)
print("Insertion Sort: Ordenado:", ordenado_insertion, "Tempo:", tempo_insertion)
print("Merge Sort: Ordenado:", ordenado_merge)