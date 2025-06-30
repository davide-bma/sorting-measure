"""
Funzioni per la misurazione dei tempi di esecuzione:
"""
import time
import random

# funzione data per stimare la risoluzione del clock
def resolution():
    start = time.perf_counter()
    # ciclo fino a quando il valore cambia
    while time.perf_counter() == start:
        pass
    stop = time.perf_counter()
    return stop - start

"""
Misura il tempo medio di esecuzione dell'algoritmo passato come parametro su array di lunghezza n
con valori casuali in [1, m], includendo il tempo di inizializzazione.
- algorithm: parametro per passare l'algoritmo
- n: dimensione dell'array
- m: valore massimo degli elementi
- min_time: tempo minimo totale per garantire errore relativo ≤ 0.001

Restituisce il tempo medio (in secondi).
"""

def measure(algorithm, n, m, min_time):
    # contatore dei test effettuati
    count = 0
    # acquisisce il tempo iniziale usando un clock monotono ad alta risoluzione
    # (funzione perf_counter come consigliata dalle specifiche fornite)
    start_time = time.perf_counter()
    # usa un ciclo infinito per continuare a effettuare misurazioni fino al raggiungimento di min_time
    while True:
        arr = [random.randint(1, m) for _ in range(n)]
        algorithm(arr)
        count += 1
        elapsed = time.perf_counter() - start_time
        if elapsed >= min_time:
            return elapsed / count