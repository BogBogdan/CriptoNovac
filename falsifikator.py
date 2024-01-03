import random
import sqlite3
from qiskit import QuantumCircuit, execute, Aer


class Falsifikator:
    def __init__(self):
        self.db_conn = sqlite3.connect('novcanice.db')
        self.db_cursor = self.db_conn.cursor()
        self.simulator = Aer.get_backend('qasm_simulator')
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS novcanice 
                                  (serijski_broj TEXT, kvantno_stanje TEXT)''')


    def generisi_kvantno_stanje(self):
        circuit = QuantumCircuit(1, 1)
        circuit.h(0)
        circuit.measure(0, 0)

        result = execute(circuit, self.simulator, shots=1).result()

        measured_bit = result.get_counts(circuit)
        return measured_bit

    def generisi_nasumicne_kvantne_brojeve(self, duzina_niza):

        stringresenja=""
        for b in range(0,duzina_niza):
            brojne_rezultate = self.generisi_kvantno_stanje()
            broj_nula = brojne_rezultate.get('0', 0)
            broj_jedinica = brojne_rezultate.get('1', 0)
            if broj_nula > broj_jedinica:
                stringresenja=stringresenja + "|0>"
            if broj_jedinica > broj_nula:
                stringresenja=stringresenja + "|1>"
            
        return stringresenja

    def pokusaj_falsifikovanja(self, duzina_niza):
        kvantno_stanje = self.generisi_nasumicne_kvantne_brojeve(duzina_niza)
        print(kvantno_stanje)
        self.db_cursor.execute('SELECT * FROM novcanice WHERE kvantno_stanje = ?', (kvantno_stanje,))
        return self.db_cursor.fetchone()

#falsifikator = Falsifikator()
#print(falsifikator.pokusaj_falsifikovanja(3))

