class Compte:
    def __init__(self, numéro_de_compte: str, titulaire_du_compte: str, solde_initial: float = 0.0):
        """Initialise un compte bancaire en FCFA"""
        self.numéro_de_compte = numéro_de_compte
        self.titulaire_du_compte = titulaire_du_compte
        self.solde_du_compte = solde_initial

    def deposit(self, montant: float) -> None:
        """Dépôt de montant sur le compte en FCFA"""
        if montant > 0:
            self.solde_du_compte += montant
            print(f"Dépôt de {montant:,.0f} FCFA effectué.")
        else:
            print("Erreur : le montant du dépôt doit être positif.")

    def withdraw(self, montant: float) -> float:
        """Retire un montant du compte si le solde est suffisant et retourne le nouveau solde (en FCFA)"""
        if montant <= 0:
            print("Erreur : le montant à retirer doit être positif.")
            return self.solde_du_compte

        if self.solde_du_compte >= montant:
            self.solde_du_compte -= montant
            print(f"Retrait de {montant:,.0f} FCFA effectué.")
            print(f"Nouveau solde : {self.solde_du_compte:,.0f} FCFA")
            return self.solde_du_compte
        else:
            print(f"Erreur : solde insuffisant. Solde actuel : {self.solde_du_compte:,.0f} FCFA")
            return self.solde_du_compte

    def remove(self, montant: float) -> float:
        """Alias pour withdraw - retire un montant et retourne le solde"""
        return self.withdraw(montant)

    def check_balance(self) -> float:
        """Retourne le solde actuel du compte en FCFA"""
        return self.solde_du_compte

    def display_info(self) -> None:
        """Affiche les informations du compte"""
        print(f"\n=== Compte n°{self.numéro_de_compte} ===")
        print(f"Titulaire : {self.titulaire_du_compte}")
        print(f"Solde : {self.solde_du_compte:,.0f} FCFA")


# 5.) Création d'une instance de la classe Compte
my_account = Compte("125103260", "CHEIKH DIOP", 1000000.0)  # 1,000,000 FCFA

# 6.) Utilisation des méthodes pour déposer, retirer et vérifier le solde
print("=== Opérations sur my_account ===")
my_account.display_info()

# Dépôt d'argent
my_account.deposit(500000.0)  # 500,000 FCFA
print(f"Solde après dépôt : {my_account.check_balance():,.0f} FCFA")

# Retrait d'argent (succès)
my_account.remove(300000.0)  # 300,000 FCFA
print(f"Solde après retrait : {my_account.check_balance():,.0f} FCFA")

# Tentative de retrait (échec - solde insuffisant)
my_account.remove(1500000.0)  # 1,500,000 FCFA
print(f"Solde final : {my_account.check_balance():,.0f} FCFA")

# 7.) Tests avec plusieurs instances
print("\n=== Tests avec plusieurs comptes ===")

# Création de deux autres comptes
compte_ahmed = Compte("326002511", "AHMED DIOP", 200000.0)  # 200,000 FCFA
compte_tidiane = Compte("251032601", "TIDIANE DIOP", 500000.0)  # 500,000 FCFA

# Opérations sur le compte d'AHMED
print("\n--- Compte d'AHMED DIOP ---")
compte_ahmed.display_info()
compte_ahmed.deposit(100000.0)  # 100,000 FCFA
compte_ahmed.remove(50000.0)  # 50,000 FCFA
compte_ahmed.remove(400000.0)  # 400,000 FCFA - Solde insuffisant
print(f"Solde final d'Ahmed : {compte_ahmed.check_balance():,.0f} FCFA")

# Opérations sur le compte de TIDIANE
print("\n--- Compte de TIDIANE ---")
compte_tidiane.display_info()
compte_tidiane.deposit(-50000.0)  # Dépôt négatif (erreur)
compte_tidiane.remove(-20000.0)  # Retrait négatif (erreur)
compte_tidiane.deposit(300000.0)  # 300,000 FCFA
print(f"Solde final de Tidiane : {compte_tidiane.check_balance():,.0f} FCFA")

# Affichage de tous les soldes
print("\n=== Synthèse des soldes ===")
print(f"My Account ({my_account.titulaire_du_compte}) : {my_account.check_balance():,.0f} FCFA")
print(f"Ahmed ({compte_ahmed.titulaire_du_compte}) : {compte_ahmed.check_balance():,.0f} FCFA")
print(f"Tidiane ({compte_tidiane.titulaire_du_compte}) : {compte_tidiane.check_balance():,.0f} FCFA")
