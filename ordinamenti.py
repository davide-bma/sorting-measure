"""
Implementazione dei quattro algoritmi di ordinamento:
- quick_sort
- quick_sort_3way
- counting_sort
- merge_sort
"""

########################################################quick_sort######################################################

def quick_sort_func(a, p, q):
    if p < q:
        # partiziona il vettore e restituisce l’indice del pivot
        pi = partition(a, p, q)
        # ordina ricorsivamente la parte sinistra
        quick_sort_func(a, p, pi)
        # ordina ricorsivamente la parte destra
        quick_sort_func(a, pi + 1, q)

# questa versione di partition usa come pivot l'elemento al centro, riducendo gli sbilanciamenti con m piccolo
def partition(a, p, q):
    # calcolo del pivot e inizializzazione degli indici per spostarsi nel vettore
    pivot = a[(p + q) // 2]
    i = p - 1
    j = q + 1

    while True:
        i += 1
        while a[i] < pivot:
            i += 1
        j -= 1
        while a[j] > pivot:
            j -= 1
        # se i due puntatori si incontrano restituisce j come punto di separazione delle due partizioni
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]

# wrapper
def quick_sort(arr):
    quick_sort_func(arr, 0, len(arr) - 1)
    return arr

#######################################################quick_sort_3way##################################################

def sort_3way(arr, p, q):
    # caso base
    if p >= q:
        return

    # lt: confine “< pivot” - i: cursore corrente - gt: confine “> pivot”
    lt, i, gt = p, p + 1, q

    pivot = arr[p]

    while i <= gt:
        if arr[i] < pivot:
            # se arr[i] appartiene alla zona “< pivot” lo spostiamo a sinistra
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            # se arr[i] appartiene alla zona “> pivot” lo spostiamo a destra
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
            # i non avanza, perché l’elemento che arriva da gt va ancora controllato
        else:
            # se arr[i] è uguale al pivot è già al posto giusto
            i += 1

    # ordino la parte sinistra
    sort_3way(arr, p, lt - 1)
    # ordino la parte destra
    sort_3way(arr, gt + 1, q)

# wrapper
def quick_sort_3way(arr):
    sort_3way(arr, 0, len(arr) - 1)
    return arr

########################################################counting_sort###################################################

def counting_sort(arr, max_value=None):

    n = len(arr)
    # caso base
    if n == 0:
        return []

    min_value = min(arr)
    max_elem  = max(arr)

    # se l’utente non ha fornito un valore massimo lo aggiorna con quello calcolato sopra
    if max_value is None or max_value < max_elem:
        max_value = max_elem

    # calcoliamo un offset per gestire eventuali valori negativi (per questo specifico progetto non
    # sarebbe richiesto, ma per passare i test sul server moodle è necessario)

    # se min_value < 0 (quindi ho numeri negativi) shifta tutti gli indici di -min_value
    offset = -min_value if min_value < 0 else 0
    # aggiorrna la dimensione in base all'offset
    size = max_value + offset + 1

    C = [0] * size
    # conta quante volte appare ogni valore
    for j in range(n):
        C[arr[j] + offset] += 1

    # accumula in C
    for j in range(1, len(C)):
        C[j] += C[j - 1]

    # costruisce l'array di output (senza perdita di dati dall'array iniziale)
    B = [0] * n
    # scorre arr da destra a sinistra per garantire la stabilità
    for i in range(n - 1, -1, -1):
        index = arr[i] + offset
        # posiziona arr[i] nella posizione corretta in B
        B[C[index] - 1] = arr[i]
        # decrementa il conteggio per gestire eventuali duplicati
        C[index] -= 1

    return B

########################################################merge_sort######################################################

def merge(arr, p, r, q):

    i = p
    j = r + 1
    # B è l’array temporaneo che conterrà l'unione delle due partizioni
    B = [0] * (q - p + 1)

    for k in range(q - p + 1):
        # se la prima metà è vuota, continua dalla seconda
        if i > r:
            B[k] = arr[j]
            j += 1
        # se la seconda metà è vuota, continua dalla prima
        elif j > q:
            B[k] = arr[i]
            i += 1
        else:
            # altrimenti confronta i due elementi correnti
            if arr[i] < arr[j]:
                B[k] = arr[i]
                i += 1
            else:
                B[k] = arr[j]
                j += 1

    # copia i valori ordinati da B nell’array originale
    for k in range(q - p + 1):
        arr[p + k] = B[k]


def merge_sort_func(arr, p, q):
    if p < q:
        r = (p + q) // 2

        # ordino ricorsivamente la prima metà
        merge_sort_func(arr, p, r)
        # ordino ricorsivamente la seconda metà
        merge_sort_func(arr, r + 1, q)

        # unisco le due metà già ordinate
        merge(arr, p, r, q)

# wrapper
def merge_sort(arr):
    merge_sort_func(arr, 0, len(arr) - 1)
    return arr