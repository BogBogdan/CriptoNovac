from emitent import Emitent

class Korisnik:
    def __init__(self, emitent):
        self.emitent = emitent

    def zahtevaj_novcanicu(self, kubiti):
        # Korisnik šalje zahtev za izdavanje novčanice
        data_string = self.emitent.izdaj_novcanicu(kubiti)
        data_tuple = eval(str(data_string))
        prvi_broj = data_tuple[0]
        return prvi_broj

    def verifikuj_novcanicu(self, novcanica_id):
        # Korisnik šalje zahtev za verifikaciju novčanice
        verifikacija = self.emitent.verifikuj_novcanicu(novcanica_id)
        return verifikacija


# Pretpostavljamo da je klasa Emitent već definisana i implementirana
#emitent = Emitent()
#korisnik = Korisnik(emitent)

# Korisnik zahteva novčanicu
#novcanica_id = korisnik.zahtevaj_novcanicu(8)
#print("ID izdate novčanice:", novcanica_id)

# Korisnik verifikuje novčanicu
#verifikacija = korisnik.verifikuj_novcanicu(novcanica_id)
#print("Rezultat verifikacije:", verifikacija)