login = "azerty"
password = "123456"

login_saisi    = input("saisir votre login : ")
password_saisi = input("saisir votre password : ")

verif = login == login_saisi and password == password_saisi

print(verif)