import tkinter as tk
from tkinter import ttk
from emitent import Emitent
from falsifikator import Falsifikator
from korisnik import Korisnik
# Pretpostavljamo da su klase Emitent i Falsifikator već definisane
# emitent = Emitent()
# falsifikator = Falsifikator()

class KvantnaBankaApp:
    def __init__(self, master, emitent, korisnik, falsifikator):
        self.master = master
        master.title("Kvantna Banka")

        # Postavljanje okvira za dugmad
        frame1 = tk.Frame(master)
        frame1.pack(pady=10)

        self.btn_izdaj_novcanicu = tk.Button(frame1, text="Izdaj Novčanicu", command=lambda: self.izdaj_novcanicu(korisnik))
        self.btn_izdaj_novcanicu.pack(side=tk.LEFT, padx=5)

        self.btn_pregled_novcanica = tk.Button(frame1, text="Pregled Novčanica", command=lambda: self.pregled_novcanica(emitent))
        self.btn_pregled_novcanica.pack(side=tk.LEFT, padx=5)

        frame2 = tk.Frame(master)
        frame2.pack(pady=10)

        self.btn_verifikuj_novcanicu = tk.Button(frame2, text="Verifikuj Novčanicu", command=lambda: self.verifikuj_novcanicu(korisnik))
        self.btn_verifikuj_novcanicu.pack(side=tk.LEFT, padx=5)

        self.btn_falsifikuj = tk.Button(frame2, text="Pokušaj Falsifikovanja", command=lambda: self.falsifikuj(falsifikator))
        self.btn_falsifikuj.pack(side=tk.LEFT, padx=5)

        # Textbox za unos podataka
        self.unos_polje = tk.Entry(frame2)
        self.unos_polje.pack(side=tk.RIGHT, padx=10)

        # Postavljanje okvira za donji deo prozora
        donji_frame = tk.Frame(master)
        donji_frame.pack(fill=tk.BOTH, expand=True)

        # Tekstualni prozor za ispis
        self.text_output = tk.Text(donji_frame, height=15, width=100)  # Povećana veličina
        self.text_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


    def izdaj_novcanicu(self, korisnik):
        novcanica_id = korisnik.zahtevaj_novcanicu(8)
        self.text_output.insert(tk.END, f"ID izdane novčanice: {novcanica_id}\n")
        pass

    def pregled_novcanica(self, emitent):
        svenovcanice = emitent.ispisi_sve_novcanice()
        self.text_output.insert(tk.END, f"Izdate novcanice\n")
        for novcanica in svenovcanice:
            self.text_output.insert(tk.END, f"Serijski broj: {novcanica[0]} Kvantno stanje: {novcanica[1]}\n")
        pass

    def verifikuj_novcanicu(self, korisnik):
        broj = self.unos_polje.get()
        verifikacija = korisnik.verifikuj_novcanicu(int(broj))
        if(verifikacija==None):
            self.text_output.insert(tk.END, f"Verifikacija nije uspela\n")
        else:
            self.text_output.insert(tk.END, f"Novcanica je verifikovana\n")
            self.text_output.insert(tk.END, f"Serijski broj: {verifikacija[0]} Kvantno stanje: {verifikacija[1]}\n")
        pass

    def falsifikuj(self, falsifikator):
        broj = self.unos_polje.get()
        falsifikat = falsifikator.pokusaj_falsifikovanja(int(broj))
        if(falsifikat==None):
            self.text_output.insert(tk.END, f"Falsifikovanje nije uspelo\n")
        else:
            self.text_output.insert(tk.END, f"Novcanica je falsifikovana\n")
            self.text_output.insert(tk.END, f"Serijski broj: {falsifikat[0]} Kvantno stanje: {falsifikat[1]}\n")
        pass

# Pokretanje aplikacije
emitent = Emitent()
korisnik = Korisnik(emitent)
falsifikator = Falsifikator()

root = tk.Tk()
mapp = KvantnaBankaApp(root,emitent,korisnik,falsifikator)
root.mainloop()
