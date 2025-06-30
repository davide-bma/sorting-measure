"""
Script principale per lanciare le misurazioni e salvare i dati.
"""

# gestisce la creazione di cartelle
import os
# crea i file .csv dove si salvano i dati
import csv

# importa gli algoritmi di ordinamento e le funzioni di misurazione
from ordinamenti import quick_sort, quick_sort_3way, counting_sort, merge_sort
from misurazioni import resolution, measure

# produce le liste di valori di n ed m seguendo la formula della serie geometrica data nelle specifiche
def generate_geometric(A, B, num=99):
    return [int(A * (B ** i) ) for i in range(num)]

def main():
    # Crea directory dati se non esistente
    os.makedirs("output/dati", exist_ok=True)

    # calcola risoluzione del clock e Tmin
    R = resolution()
    # formula data dalle specifiche
    Tmin = R * 10

    # costanti per n
    A_n = 100
    B_n = (100000 / 100) ** (1/99)

    # costanti per m
    A_m = 10
    B_m = (1000000 / 10) ** (1/99)

    n_values = generate_geometric(A_n, B_n)
    m_values = generate_geometric(A_m, B_m)

    # misure dei tempi per tutti gli n con m fisso
    with open("output/dati/tempi_vs_n.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "quick_sort", "quick_sort_3way", "counting_sort", "merge_sort"])
        for n in n_values:
            t_qs = measure(quick_sort, n, 100000, Tmin)
            t_qs3 = measure(quick_sort_3way, n, 100000, Tmin)
            t_cs = measure(counting_sort, n, 100000, Tmin)
            t_ms = measure(merge_sort, n, 100000, Tmin)
            writer.writerow([n, t_qs, t_qs3, t_cs, t_ms])

    # misure dei tempi per tutti gli m con n fisso
    with open("output/dati/tempi_vs_m.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["m", "quick_sort", "quick_sort_3way", "counting_sort", "merge_sort"])
        for m in m_values:
            t_qs = measure(quick_sort, 10000, m, Tmin)
            t_qs3 = measure(quick_sort_3way, 10000, m, Tmin)
            t_cs = measure(counting_sort, 10000, m, Tmin)
            t_ms = measure(merge_sort, 10000, m, Tmin)
            writer.writerow([m, t_qs, t_qs3, t_cs, t_ms])

if __name__ == "__main__":
    main()
