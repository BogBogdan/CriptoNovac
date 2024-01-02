# Instalacija Qiskit-a (ako već nije instaliran)
# !pip install qiskit

from qiskit import QuantumCircuit, Aer, execute
import sqlite3
import random

class Emitent:
    def __init__(self):
        # Inicijalizacija baze podataka
        self.db_conn = sqlite3.connect('novcanice.db')
        self.db_cursor = self.db_conn.cursor()
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS novcanice 
                                  (serijski_broj TEXT, kvantno_stanje TEXT)''')

    def generisi_serijski_broj(self):
        # Generisanje jedinstvenog četvorocifrenog serijskog broja
        return str(random.randint(1000, 9999))

    def generisi_kvantno_stanje(self):
        # Generisanje kvantnog stanja kubita
        qc = QuantumCircuit(1, 1)  # Dodajemo 1 klasični bit za merenje
       
        qc.h(0)  

        qc.measure(0, 0)  

        backend = Aer.get_backend('qasm_simulator')
        rezultati = execute(qc, backend, shots=3).result()
        brojne_rezultate = rezultati.get_counts(qc)

        broj_nula = brojne_rezultate.get('0', 0)
        broj_jedinica = brojne_rezultate.get('1', 0)

        if broj_nula > broj_jedinica:
            return "|0>"
        if broj_jedinica > broj_nula:
            return "|1>"
        
        return None

    def izdaj_novcanicu(self, kubiti=1):

        kvantno_stanje=""
        for _ in range(0,kubiti):
            kvantno_stanje = kvantno_stanje + self.generisi_kvantno_stanje()
        serijski_broj = self.generisi_serijski_broj()

        self.db_cursor.execute('INSERT INTO novcanice VALUES (?, ?)', (serijski_broj, str(kvantno_stanje)))
        self.db_conn.commit()
        return serijski_broj, kvantno_stanje

    def ispisi_sve_novcanice(self):
        # Ispisuje sve novčanice iz baze
        self.db_cursor.execute('SELECT * FROM novcanice')
        sve_novcanice = self.db_cursor.fetchall()
        return sve_novcanice
        

    def verifikuj_novcanicu(self, serijski_broj):
        # Verifikacija novčanice
        self.db_cursor.execute('SELECT * FROM novcanice WHERE serijski_broj = ?', (serijski_broj,))
        return self.db_cursor.fetchone()

    def __del__(self):
        self.db_conn.close()

# Primer upotrebe
# emitent = Emitent()
# novcanica = emitent.izdaj_novcanicu(2)
# print("Izdali smo novčanicu:", novcanica)
