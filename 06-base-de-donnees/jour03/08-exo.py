ville_saisie = input("Quelle est votre ville de naissance : ")

if ville_saisie == "Paris":
    print("Vous habitez à Paris")
elif ville_saisie == "Boulogne" or ville_saisie == "Montrouge" or ville_saisie == "Clamart":
    print("Vous habitez dans le 92")
else :
    print("Ville inconnue")


liste_ville_92 = ["Boulogne" , "Montrouge" , "Clamart" ]

if ville_saisie == "Paris":
    print("Vous habitez à Paris")
elif ville_saisie in  liste_ville_92 :
    print("Vous habitez dans le 92")
else :
    print("Ville inconnue")