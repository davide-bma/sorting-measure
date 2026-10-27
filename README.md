# Sorting Measure

Un'applicazione in Python progettata per **misurare, confrontare e visualizzare graficamente le prestazioni di diversi algoritmi di ordinamento** al variare della dimensione dei dati di input.

Il progetto permette di analizzare empiricamente la complessità computazionale (Time Complexity) degli algoritmi, confrontando i tempi di esecuzione reali con i modelli teorici della notazione Big O.

---

## 📂 Struttura del Progetto

Il codice è organizzato in moduli separati per garantire alta coerenza e modularità:

*   **`main.py`**: Il punto di ingresso dell'applicazione che coordina il flusso del programma (generazione dati, esecuzione benchmark e avvio dei grafici).
*   **`ordinamenti.py`**: Contiene le implementazioni dei vari algoritmi di ordinamento oggetto di studio (es. Bubble Sort, Quick Sort, Merge Sort, Insertion Sort, ecc.).
*   **`misurazioni.py`**: Gestisce la logica di benchmark, calcolando i tempi di esecuzione precisi per i diversi algoritmi su array di dimensioni crescenti e in differenti scenari (caso ottimo, medio e peggiore).
*   **`grafici.py`**: Si occupa della visualizzazione dei dati raccolti generandone curve di performance e grafici comparativi.
*   **`output/`**: Cartella dedicata al salvataggio dei grafici generati (es. in formato PNG) e dei report delle misurazioni.
