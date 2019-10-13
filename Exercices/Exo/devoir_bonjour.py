print("Bonjour")
answer = input("Est-ce que tu vas bien ? ")
if not (answer == "Oui" or answer == "oui" or answer == "Non" or answer == "non"):
    print("Vous deviez répondre par oui ou non.")
    answer = input("Est-ce que tu vas bien ? ")
if (answer == "oui" or answer == "Oui"):
    print("Super. Bonne Journée !")
else:
    print("Courage, ça ira bientôt mieux !")