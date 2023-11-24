from gestion_employes import Employe

employe1 = Employe('LUBA1-ANG', 'Merveille', 25000)
employe1.show_detail_employ()
employe1.generate_email_address()
employe1.increase_salary_percentage(5)
employe1.show_detail_employ()

employe1.change_salary('Merveille', 50000)
employe1.change_salary('Merveille', 20000)
