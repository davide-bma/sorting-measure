"""
Script per generare automaticamente grafici comparativi dai dati prodotti salvati in file CSV.
Genera:
- tempi_vs_n_linear.png: grafico lineare (asse X lineare)
- tempi_vs_n_loglog.png: grafico log-log
- tempi_vs_m_linear.png: grafico lineare
- tempi_vs_m_loglog.png: grafico log-log
"""

import os
import csv
import matplotlib.pyplot as plt

def read_csv_to_dicts(csv_path):
    """
    Legge un CSV e ritorna una lista di dict, con chiavi
    prese dalla prima riga (intestazioni) e valori float.
    """
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        return [
            { key: float(value) for key, value in row.items() }
            for row in reader
        ]

def plot_comparison(data, x_key, alg_keys, title, output_path, log_scale=False):
    """
    Disegna un grafico comparativo:
      - data: lista di dict (come da read_csv_to_dicts)
      - x_key: nome della colonna da usare in ascissa ('n' o 'm')
      - alg_keys: lista dei nomi delle colonne da plottare
      - title: titolo del grafico
      - output_path: percorso dove salvare il PNG
      - log_scale: se True imposta asse X e Y in scala logaritmica
    """
    plt.figure()
    for alg in alg_keys:
        xs = [row[x_key] for row in data]
        ys = [row[alg] for row in data]
        plt.plot(xs, ys, label=alg)
    plt.xlabel(x_key)
    plt.ylabel("Tempo medio (s)")
    plt.title(title)
    plt.legend()

    # ---- attiva la griglia su righe e colonne ----
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    if log_scale:
        plt.xscale('log')
        plt.yscale('log')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # Directory di input (CSV) e output (figure)
    dati_dir    = 'output/dati'
    grafici_dir = 'output/relazione/grafici'
    os.makedirs(grafici_dir, exist_ok=True)

    # Percorsi ai CSV
    file_n = os.path.join(dati_dir, 'tempi_vs_n.csv')
    file_m = os.path.join(dati_dir, 'tempi_vs_m.csv')

    # Carica i dati
    data_n = read_csv_to_dicts(file_n)
    data_m = read_csv_to_dicts(file_m)

    # Nomi delle colonne degli algoritmi
    algs = ['quick_sort', 'quick_sort_3way', 'counting_sort', 'merge_sort']

    # Grafici su n
    plot_comparison(
        data_n,
        x_key='n',
        alg_keys=algs,
        title='Tempo medio vs n (scala lineare)',
        output_path=os.path.join(grafici_dir, 'tempi_vs_n_linear.png'),
        log_scale=False
    )
    plot_comparison(
        data_n,
        x_key='n',
        alg_keys=algs,
        title='Tempo medio vs n (scala log-log)',
        output_path=os.path.join(grafici_dir, 'tempi_vs_n_loglog.png'),
        log_scale=True
    )

    # Grafici su m
    plot_comparison(
        data_m,
        x_key='m',
        alg_keys=algs,
        title='Tempo medio vs m (scala lineare)',
        output_path=os.path.join(grafici_dir, 'tempi_vs_m_linear.png'),
        log_scale=False
    )
    plot_comparison(
        data_m,
        x_key='m',
        alg_keys=algs,
        title='Tempo medio vs m (scala log-log)',
        output_path=os.path.join(grafici_dir, 'tempi_vs_m_loglog.png'),
        log_scale=True
    )

if __name__ == '__main__':
    main()
