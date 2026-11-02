def introducere():
    print("Bun venit! Eu sunt colectorul. O sa am nevoie de niste informatii pentru a iti face un profil.")
    confirmare=input("Pentru a continua tasteaza mesajul ,, Confirm ,, ")
    print("Raspunsul tau este {confirmare} acum vom continua cu colectarea informatiilor.")
def carte_de_vizita():
    nume=input("Inrodu numele tau: ")
    varsta=input("Inrodu data nasterii: ")
    hobby=input("Introdu hobbyul tau preferat: ")
    print(f"Numele meu este {nume}.")
    print(f"M-am nascut in data de {varsta}.")
    print(f"Hobbyul meu preferat este {hobby}.")
introducere()
carte_de_vizita()
