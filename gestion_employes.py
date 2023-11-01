class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    # methode permettant de voir les details d'un employés
    def show_detail_employ(self):
        print(f"L'employe {self.nom} {self.prenom} a un salaire de {self.salaire} €.")

    # methode permettant de definir ou de modofier le salaire d'un employé
    def change_salary(self, new_salary):
        self.salaire = new_salary


#employe1 = Employe("LUBA", "Merveille", 25000)

#employe1.show_detail_employ()
#employe1.change_salary(500)
#employe1.show_detail_employ()




    # methode permettant de générer l'adresse Email de l'employé
    def generate_email_address(self):
        print(f"Ladresse Email de {self.nom} est {self.prenom}.{self.nom}@entreprise.com")
