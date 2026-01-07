class Car:
    def __init__(self, model: str = "geen model", jaartal: int = 2001, kleur: str = "geen kleur", pk: int = 90):
        if not isinstance(jaartal, int):
            raise TypeError("Het jaartal moet een geheel getal zijn.")
        if not isinstance(pk, int):
            raise TypeError("PK moet een geheel getal zijn.")
        
        
        self.model = model
        self.jaartal = jaartal
        self.kleur = kleur
        self.pk = pk

    def __repr__(self):
        return f"Model: {self.model}\nJaar: {self.jaartal}\nKleur: {self.kleur}\nPK: {self.pk}\n"
    
    def krijg_info(self):
        return f"""Je hebt volgende informatie ingegeven:
        Auto informatie: {self.model}
        Jaartal: {self.jaartal}
        Kleur: {self.kleur}
        Pk: {self.pk}"""
    
    @staticmethod
    def krijg_info_car():
        model = input("Geef het model van de wagen in: ")

        while True:
            try:
                jaartal = int(input("Geef het jaartal van de wagen in: "))
                break
            except ValueError:
                print("FOUT: Voer een geldig jaartal in!")
                                                                
        kleur = input("Geef de kleur van de wagen: ")

        while True:
            try:
                pk = int(input("Geef het aantal PK in de wagen: "))
                if pk < 1 or pk > 1000:
                    print("FOUT: Pk moet tussen 1-1000 liggen!")
                    continue
                break
            except ValueError:
                print("FOUT: Voer een geldig getal in voor PK!")
            
        return Car(model, jaartal, kleur, pk)