from random import randint
import time

User_Score = Bot_Score = 0
PPS = ["1", "2", "3"]
NON = ["non", "Non", "NO", "N", "n", "NON", "No", "NoN"]
OUI = ["oui", "Oui", "OUI", "o", "O", "OUi", "OuI"]
Max_point = 3

def Mb(s,t):
    time.sleep(s)
    print(t)


input("*...*")

print("Bonjour !")
Mb(2, "Hmm...")
Mb(1, "On se connait ?")
Mb(1.3, "Non je ne pense pas...")
time.sleep(1)
user_name = input("Voudrais tu me partager ton nom ? (o/n)")
if user_name in OUI:
    user_name = input("Super ! Dit le moi : ")
elif user_name in NON:
    Mb(1.5, "Ha...")
    Mb(1, "...")
    user_name = "Flibul Du Pondibul"
    Mb(2, "Et bien je vais t'appeler Flibul Du Pondibul, d'accord ? (oui/non)")
    Mb(2, "Enfaite tu n'as plus le choix maintenant HAHAHAHA")
else:
    time.sleep(1)
    Mb(1.5, "Pardon???")
    Mb(1.5, "Moi pas parler même langue que toi")
    Mb(2, "Du coup, je vais t'appeller...")
    user_name = "BLOUBLOU"
    Mb(2, "BLOUBLOU !")
    Mb(1,"Bon bref...")
if user_name in ["Alex", "Alexou", "Xouxou"]:
    Mb(1, "HA, mais bien-sûr, vous êtes Dame Alex...")
    Mb(1,"Maitre Diego m'a tant parlé de vous...")
    Mb(1, "Et il disait vrai en disant que vous êtes d'une beauté exeptionnel...")
    Mb(2,"Enfaite je peux pas savoir, je suis un ordinateur")


time.sleep(1.5)
Mb(1.5, f"Bonjour {user_name} !")
Mb(1.5, "Tu viens de lancer...")
def ppc(t):
    print(
    """
           .__                            
    ______ |__| __________________  ____  
    \____ \|  |/ __ \_  __ \_  __ \/ __ \ 
    |  |_> >  \  ___/|  | \/|  | \\  ___/ 
    |   __/|__|\___  >__|   |__|   \___  >
    |__| 
    """)
    time.sleep(t)
    print(
    """
                        .__              
    ___________  ______ |__| ___________ 
    \____ \__  \ \____ \|  |/ __ \_  __ \ 
    |  |_> > __ \_  |_> >  \  ___/|  | \/
    |   __(____  |   __/|__|\___  >__|   
    |__|         |__|      
    """)
    time.sleep(t)
    print(
    """
           .__                                   
    ___  _ |__| ______ ____ _____   __ _____  ___
    _/ ___\|  |/  ___// __ \\__  \ |  |  \  \/  /
    \  \___|  |\___ \\  ___/ / __ \_  |  />    < 
     \____/|__/______\\_____\____  |____//__/\_ \ 

    """)
    time.sleep(t)
ppc(0.7)
Mb(0,"Mais avant de jouer, Je vais me présenter." )
Mb(2, "Je m'appelle Mr Bot ")
Mb(1.5, "Et en te frottant à ce programme magique...")
Mb(2, "Tu viens de me défier à un jeu bien particulier...")
Mb(2, "Le...")
time.sleep(1)
ppc(0.7)

if input("Voudrais tu connaitres les règles de ce jeu ? ") in OUI:
    time.sleep(1)
    Mb(2, "Bien...")
    Mb(1.5, "Je vais te présenter les règle du...")
    time.sleep(2)
    ppc(0.7)
    print("Ce jeu se joue en tour par tour,")
    Mb(2,"Tu as trois armes à ta disposition,")
    Mb(2,"Ces trois armes sont...")
    ppc(1.5)
    print("La pierre bat les ciseaux")
    Mb(2,"Le papier bat la pierre")
    Mb(2,"Les ciseaux battent le papier")
    Mb(2,"Tu vas voir, c'est très facile à comprendre !")
    Mb(2, "HA, j'ai oublié de te dire qu'au...")
    ppc(0.7)
    print("Le premier à trois points gagne la partie")
    Mb(2,"Je te souhaite bonne chance !")
Mb(2, "C'est parti !!!")

while True :
    user = ""
    while user not in PPS :
        user = input("Pierre (1), Papier (2) ou Ciseaux (3) ? ")
    user = int(user)
    bot = randint(1,3)


    if user == 2 and bot == 1:
        User_Score +=1
    elif user == 1 and bot == 3:
        User_Score +=1
    elif user == 3 and bot == 2:
        User_Score +=1
    elif bot == 1 and user == 3 :
        Bot_Score +=1
    elif bot == 2 and user == 1 :
        Bot_Score +=1
    elif bot == 3 and user == 2 :
        Bot_Score +=1
    
    if user == 1:
        user = "Pierre"
    elif user == 2:
        user = "Papier"
    else:
        user = "Ciseaux"
    if bot == 1:
        bot = "Pierre"
    elif bot == 2:
        bot = "Papier"
    else:
        bot = "Ciseaux"

    print("_" * 50)
    print("ATTENTION...")
    for i in ["Pierre...", "Papier...", "Ciseaux..."]:
        time.sleep(0.7)
        print(i)
    time.sleep(1)
    print(f"""
    {user} ⚡ {bot}""")
    print(f"""
    {user_name} : {User_Score}
    Mr Bot : {Bot_Score}""")
    if user == bot:
        print("égalité...")


    if User_Score == Max_point :
        print(f"Félicitation {user_name}, vous avez gagné le...")
        time.sleep(1)
        User_Score = Bot_Score = 0
        ppc(0.7)
        Rstrt = input("Voulez-vous redéfier Mr Bot ? ")
        if Rstrt in OUI:
            Mb(1,f"Très bien {user_name}, je suis prêt pour jouer à ce magnifique jeu qui est...")
            Mb(2.5,"Le...")
            time.sleep(2)
            ppc(0.7)
            
        elif Rstrt in NON:
            Mb(1,f"Très bien {user_name}, je t'attendrais...")
            Mb(2.5,"Ou je vais attendre pour que Diego m'améliore...")
            Mb(2,"Enfin bref, j'espère que tu as aimé joué à...")
            time.sleep(2)
            ppc(0.7)
            Mb(1, f"À bientôt {user_name} !")
            break
        else:
            Mb(1, "Hmm...")
            Mb(1, "J'ai pas compris")
            Mb(1, "Je prends ça pour un non")
            Mb(1, f"À bientôt {user_name} !")
            break
    elif Bot_Score == Max_point :
        print("Dommage... Mr Bot est trop fort pour toi...")
        User_Score = Bot_Score = 0
        Rstrt = input("Voulez-vous redéfier Mr Bot ? ")
        if Rstrt in OUI:
            Mb(1,f"Très bien {user_name}, je suis prêt pour jouer à un jeu...")
            Mb(2.5,"Le...")
            time.sleep(2)
            ppc(0.7)
            
        elif Rstrt in NON:
            Mb(1,f"Très bien {user_name}, je t'attendrais...")
            Mb(2.5,"Ou je vais attendre pour que Diego m'améliore...")
            Mb(2,"Enfin bref, j'espère que tu as aimé joué à...")
            time.sleep(2)
            ppc(0.7)
            Mb(1, f"À bientôt {user_name} !")
            break
        else:
            Mb(1, "Hmm...")
            Mb(1, "J'ai pas compris")
            Mb(1, "Je prends ça pour un non")
            Mb(1, f"À bientôt {user_name} !")
            print("_" * 50)
            break
print("Fin de partie.")
