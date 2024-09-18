name = input("quel est votre nom ?")

age = 0

while age == 0:
    age_str = input("quel est votre age ?")
    try:
        age = int(age_str)
    except:
        print("veuillez entrer un age valide")

print("Vous vous appelez "+ name+ " et vous avez "+ str(age) + " ans, l'année prochaine vous aurez "+ str(age +1)+ " ans")

