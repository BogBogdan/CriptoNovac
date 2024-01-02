import random
import sqlite3

class Falsifikator:
    def __init__(self):
        self.db_conn = sqlite3.connect('novcanice.db')
        self.db_cursor = self.db_conn.cursor()
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS novcanice 
                                  (serijski_broj TEXT, kvantno_stanje TEXT)''')

    def generisi_nasumicne_kvantne_brojeve(self, duzina_niza):
        kvantna_stanja = ["|0>", "|1>"]
        nasumicni_niz = ''.join(random.choice(kvantna_stanja) for _ in range(duzina_niza))
        return nasumicni_niz

    def pokusaj_falsifikovanja(self, duzina_niza):
        kvantno_stanje = self.generisi_nasumicne_kvantne_brojeve(duzina_niza)
        self.db_cursor.execute('SELECT * FROM novcanice WHERE kvantno_stanje = ?', (kvantno_stanje,))
        return self.db_cursor.fetchone()


# falsifikator = Falsifikator()
# broj_kubita = 3  # Primer za kvantnu novčanicu sa 3 kubita
# uspesnost_falsifikovanja = falsifikator.pokusaj_falsifikovanja(broj_kubita)
# print(f"Uspesnost falsifikovanja za {broj_kubita} kubita: {uspesnost_falsifikovanja:.2f}")
