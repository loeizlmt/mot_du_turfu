# on importe les bibliothèques nécessaires
import streamlit as st
import random
from streamlit.components.v1 import html

# Titre et sous-titre
st.title("Évaluateur de mot de passe")

# Texte d'introduction
st.write("Bienvenue sur cette application qui vous permet d'évaluer et de générer de mots de passe.")

# Ajout d'une image
st.image("image.png", caption="Logo")

# déclaration des variables
mot_de_passe_gen= "" # mot de passe généré
score = 0 # score du mot de passe
mot_de_passe_longeur = False # vérification de la longueur du mot de passe
scoremaj = False # vérification de la présence d'une majuscule dans le mot de passe à tester
scoremin = False # vérification de la présence d'une minuscule dans le mot de passe à tester
scorenum = False # vérification de la présence d'un chiffre dans le mot de passe à tester
scorecaractère = False # vérification de la présence d'un caractère spécial dans le mot de passe à tester
mots_interdits = False # vérification de la présence d'un mot interdit dans le mot de passe à tester
caractères = ["!", "@", "#",  "$", "%", "^", "&", "*", "(", ")"," ?", ";"] # liste des caractères spéciaux
button_cliqué = False # vérification si le bouton de test de mot de passe a été cliqué pour afficher des conseils personnalisés
maj = False # vérification de si l'utilisateur a coché la case majuscules
min =False # vérification de si l'utilisateur a coché la case minuscules
spe = False # vérification de si l'utilisateur a coché la case caractères spéciaux
num =False # vérification de si l'utilisateur a coché la case chiffres
long = 0 # longueur du mot de passe généré
js_activé = False # vérification de si le javascript a été activé

# Fonction pour générer un mot de passe
def generer_mot_de_passe(longueur, majuscules, minuscules, chiffres, speciaux):
    # si l'utilisateur souhaite mettre des majuscules dans son mot de passe on ajoute les caractères majuscules
    if majuscules :
        caracteres_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    else : caracteres_maj = ""
    # si l'utilisateur souhaite mettre des minuscules dans son mot de passe on ajoute les caractères minuscules
    if minuscules :
        caracteres_min = "abcdefghijklmnopqrstuvwxyz"  
    else: caracteres_min = ""
    # si l'utilisateur souhaite mettre des chiffres dans son mot de passe on ajoute les chiffres
    if chiffres :
        chiffres_générateur = "0123456789"  
    else: chiffres_générateur = ""
    # si l'utilisateur souhaite mettre des caractères spéciaux dans son mot de passe on ajoute les caractères spéciaux
    if speciaux :
        spéciaux_générateur = "!@#$%^&*()-_+=<>?/"  
    else : spéciaux_générateur = ""
    # si l'utilisateur n'a pas sélectionné de type de caractère on affiche un message d'erreur
    if not caracteres_maj and not caracteres_min and not chiffres_générateur and not spéciaux_générateur:
        return "Sélectionnez au moins un type de caractère."
    # création d'une liste pour mettre les caractères du mot de passe
    mot_de_passe = []
    # on ajoute un caractère de chaque type à la liste si l'utilisateur a coché la case correspondante pour être sur d'avoir le score maximal
    if majuscules:
        mot_de_passe.append(random.choice(caracteres_maj))
    if minuscules:
        mot_de_passe.append(random.choice(caracteres_min))
    if chiffres:
        mot_de_passe.append(random.choice(chiffres_générateur))
    if speciaux:
        mot_de_passe.append(random.choice(spéciaux_générateur))

    # on crée une variable qui contient tous les caractères possibles
    tous_caracteres = caracteres_maj + caracteres_min + chiffres_générateur + spéciaux_générateur
    # pour remplir le reste du mot de passe on choisi aléatoirement des caractère dans la variable tous_caractères
    # qu'on ajoute au mot de passe jusqu'à ce qu'il ait la longueur décidée par l'utilisateur
    mot_de_passe += [random.choice(tous_caracteres) for i in range(longueur - len(mot_de_passe))]
    # on renvoi tous les caractères mis bout à bout pour avoir une chaine de caractère
    return ''.join(mot_de_passe)
    
# Fonction pour évaluer le mot de passe
def score_mdp() : 
    # on récupère les variables globales dont on a besoin
    global score, mot_de_passe_longeur, scoremaj, scoremin, scorenum, scorecaractère, mots_interdits, caractères
    # si le mot de passe a une longueur de 8 caractères ou plus on ajoute 2 points
    if len(mot_de_passe) >= 8:
        score += 2
    # on met mot_de_passe_longeur à True si le mot de passe est trop court pour afficher un conseil personnalisé
    else : 
        mot_de_passe_longeur = True
    # on vérifie si le mot de passe est plus grand que 12, si c'est le cas on ajoute 2 points
    if len(mot_de_passe) >= 12 :
        score += 2
    # on vérifie si le mot de passe contient une majuscule, si c'est le cas on ajoute 1 point
    for i in mot_de_passe :
        if i.isupper() :
            if scoremaj == False :
                score += 2
                scoremaj = True # on met scrormaj à True pour ne pas ajouter plusieurs fois les points pour les majuscules
    # on vérifie si le mot de passe contient une minuscule, si c'est le cas on ajoute 2 points
    for i in mot_de_passe :
        if i.islower() :
            if scoremin == False :
                score += 1
                scoremin = True # on met scoremin à True pour ne pas ajouter plusieurs fois le point pour les minuscules
    # on vérifie si le mot de passe contient un chiffre, si c'est le cas on ajoute 2 points
    for i in mot_de_passe :
        if i.isnumeric() :
            if scorenum == False :
                score += 2
                scorenum = True # on met scorenum à True pour ne pas ajouter plusieurs fois les points pour les chiffres
    # on vérifie si le mot de passe contient un caractère spécial, si c'est le cas on ajoute 3 points
    for i in caractères :
        if i  in mot_de_passe :
            if scorecaractère == False :
                score += 3
                scorecaractère = True # on met scorecaractère à True pour ne pas ajouter plusieurs fois les points pour les caractères spéciaux
    # on vérifie si le mot de passe est dans la liste des mots interdits, si c'est le cas on enlève 5 points
    for i in lignes :
        if mot_de_passe in i :
            if mots_interdits == False :
                score += -5
                mots_interdits = True # on met mots_interdits à True pour ne pas enlever plusieurs fois les points pour les mots interdits 
                                      # même si c'est peu probable que le mot de passe contienne plusieurs mots interdits
# file contient le fichier mots_interdits.txt
file  = open("mots_interdits.txt","r",encoding="utf8")
# lignes lit le fichier qui est dans file
lignes = file.readlines()

# Zone de saisie
mot_de_passe = st.text_input("Entrez votre mot de passe :", "")

# Boutons pour évaluer le mot de passe
if st.button("évaluer mon mot de passe"):
    button_cliqué = True
    score_mdp()
    # on divise le score par 12 puis on le multiplie par 10 pour avoir un score sur 10
    score = (score / 12)*10
    # on convertit le score en entier pour ne pas avoir un float dans le slider
    score = int(score)
# Curseur qui indique le score du mot de passe
valeur_curseur = st.slider("Note de votre mot de passe :", 0, 10, score, disabled=True)
# on affiche la note du mot de passe dans un texte en plus du slider
st.write(f"Note de votre mot de passe : {valeur_curseur}")

# Conseils personnalisés si le score est en dessous de 7 et que le bouton a été cliqué
if score < 7 and button_cliqué == True :
    # si il y a un mot interdit dans le mot de passe on affiche un conseil
    if mots_interdits :
        st.write("Mot de passe trop courant, essayez de le changer")
    # si le mot de passe est trop court on affiche un conseil
    if mot_de_passe_longeur : 
        st.write("Mot de passe est trop court")
    # si le mot de passe ne contient pas de majuscule on affiche un conseil
    if scoremaj == False :
        st.write("ajoutez une majuscule")
    # si le mot de passe ne contient pas de minuscule on affiche un conseil
    if scoremin == False :
        st.write("ajoutez une minuscule")
    # si le mot de passe ne contient pas de chiffre on affiche un conseil
    if scorenum == False : 
        st.write("ajoutez un chiffre")
    # si le mot de passe ne contient pas de caractère spécial on affiche un conseil
    if scorecaractère == False : 
         st.write("ajoutez un caractère")
# si le score est supérieur ou égal à 10 on affiche un message 
if score >= 10 :
    st.write("Mot de passe très robuste !")

# on demande à l'utilisateur de choisir les options pour générer le mot de passe
st.write("Choisissez vos options pour générer le mot de passe :")
# cases à cocher pour choisir si il veut une majuscule, une minuscule, un caractère spécial ou un chiffre
if st.checkbox("majuscules") :
    maj = True # on passe maj à True pour le passer en paramètre dans la fonction generer_mot_de_passe()
if st.checkbox("minuscules") :
    min = True
if st.checkbox("caractères spéciaux") :
    spe = True
if st.checkbox("chiffres") :
    num = True

# curseur pour choisir la longueur du mot de passe
long = st.slider("Entrez le nombre de caractères souhaités :", 0, 50)

# bouton pour générer le mot de passe
if st.button("générer un mot de passe") :
    # on génère le mot de passe avec les options choisies en paramètre de la fonction generer_mot_de_passe()
    mot_de_passe_gen = (generer_mot_de_passe(long, maj, min, num, spe))
    # si l'utilisateur n'a pas sélectionné tous les types de caractères on affiche une alerte en javascript pour l'infomer 
    # que son mot de passe ne pourra pas avoir le score maximal
    if not maj or not min or not num or not spe:
        # déclaration du javascript
        my_js = """
        alert("Attention, vous n'avez pas sélectionné tous les types de caractères, votre mot de passe ne pourra donc pas avoir le score maximal.");
        """ 
        # création du html avec le javascript intégré
        my_html = f"<script>{my_js}</script>"
        js_activé = True # nous permet de savoir si on a besoin d'exécuter le javascript à la fin de la page pour ne pas avoir un espace vide
                         # entre le bouton et le mot de passe généré
# message pour informer l'utilisateur que le mot de passe a été généré
st.write("voici votre mot de passe sécurisé que vous pouvez copier")
# on affiche le mot de passe généré dans une zone de code pour pouvoir le copier facilement
st.code(mot_de_passe_gen)

# message de fin
st.write("Merci d'avoir utilisé cette application. 🚀")

# si le javascript a été activé on l'éxécute
if js_activé:
    #execution du html ici pour ne pas créer un espace vide entre le bouton et le mot de passe généré
    html(my_html)