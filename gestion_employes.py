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

    # méthode permettant d'augmenter le salaire en pourcentage
    def increase_salary_percentage(self, percentage):
        self.salaire = self.salaire * (percentage/100 + 1)
        return self.salaire

    # methode permettant de générer l'adresse Email de l'employé
    def generate_email_address(self):
        print(f"Ladresse Email de {self.nom} est {self.prenom}.{self.nom}@entreprise.com")
