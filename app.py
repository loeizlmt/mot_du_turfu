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
mot_de_passe_longeur = False #
scoremaj = False
scoremin = False
scorenum = False   
scorecaractère = False
mots_interdits = False
caractères = ["!", "@", "#",  "$", "%", "^", "&", "*", "(", ")"," ?", ";"]
button_cliqué = False
maj = False
min =False
maj = False
min =False
spe = False
num =False
long = 0
js_activé = False

import random

def generer_mot_de_passe(longueur, majuscules, minuscules, chiffres, speciaux):
    if majuscules :
        caracteres_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    else : caracteres_maj = ""
    if minuscules :
        caracteres_min = "abcdefghijklmnopqrstuvwxyz"  
    else: caracteres_min = ""
    if chiffres :
        chiffres_générateur = "0123456789"  
    else: chiffres_générateur = ""
    if speciaux :
        spéciaux_générateur = "!@#$%^&*()-_+=<>?/"  
    else : spéciaux_générateur = ""

    if not caracteres_maj and not caracteres_min and not chiffres_générateur and not spéciaux_générateur:
        return "Sélectionnez au moins un type de caractère."
    mot_de_passe = []
    if majuscules:
        mot_de_passe.append(random.choice(caracteres_maj))
    if minuscules:
        mot_de_passe.append(random.choice(caracteres_min))
    if chiffres:
        mot_de_passe.append(random.choice(chiffres_générateur))
    if speciaux:
        mot_de_passe.append(random.choice(spéciaux_générateur))

    tous_caracteres = caracteres_maj + caracteres_min + chiffres_générateur + spéciaux_générateur
    mot_de_passe += [random.choice(tous_caracteres) for _ in range(longueur - len(mot_de_passe))]
    return ''.join(mot_de_passe)
    




def score_mdp() : 
    global score, mot_de_passe_longeur, scoremaj, scoremin, scorenum, scorecaractère, mots_interdits, caractères
    if len(mot_de_passe) >= 8:
        score += 2
    else : 
        mot_de_passe_longeur = True
    if len(mot_de_passe) >= 12 :
        score += 2
    for i in mot_de_passe :
        if i.isupper() :
            if scoremaj == False :
                score += 2
                scoremaj = True
    for i in mot_de_passe :
        if i.islower() :
            if scoremin == False :
                score += 1
                scoremin = True
    for i in mot_de_passe :
        if i.isnumeric() :
            if scorenum == False :
                score += 2
                scorenum = True
    for i in caractères :
        if i  in mot_de_passe :
            if scorecaractère == False :
                score += 3
                scorecaractère = True
    for i in lignes :
        if mot_de_passe in i :
            if mots_interdits == False :
                score += -5
                mots_interdits = True

file  = open("mots_interdits.txt","r",encoding="utf8")
lignes = file.readlines()

# Zone de saisie
mot_de_passe = st.text_input("Entrez votre mot de passe :", "")

# Boutons interactifs
if st.button("évaluer mon mot de passe"):
    button_cliqué = True
    score_mdp()
if score > 10 :
    score = 10
# Curseur interactif
valeur_curseur = st.slider("Note de votre mot de passe :", 0, 10, score, disabled=True)
st.write(f"Note de votre mot de passe : {valeur_curseur}")

if score < 7 and button_cliqué == True :
    if mots_interdits :
        st.write("Mot de passe trop courant, essayez de le changer")
    if mot_de_passe_longeur : 
        st.write("Mot de passe est trop court")
    if scoremaj == False :
        st.write("ajoutez une majuscule")
    if scoremin == False :
        st.write("ajoutez une minuscule")
    if scorenum == False : 
        st.write("ajoutez un chiffre")
    if scorecaractère == False : 
         st.write("ajoutez un caractère")
if score >= 10 :
    st.write("Mot de passe très robuste !")

st.write("Choisissez vos options pour générer le mot de passe :")
if st.checkbox("majuscules") :
    maj = True
if st.checkbox("minuscules") :
    min = True
if st.checkbox("caractères spéciaux") :
    spe = True
if st.checkbox("chiffres") :
    num = True
long = st.slider("Entrez le nombre de caractères souhaités :", 0, 50)

if st.button("générer un mot de passe") :
    mot_de_passe_gen = (generer_mot_de_passe(long, maj, min, num, spe))
    if not maj or not min or not num or not spe:
        # déclaration du javascript
        my_js = """
        alert("Attention, vous n'avez pas sélectionné tous les types de caractères, votre mot de passe ne pourra donc pas avoir le score maximal.");
        """ 
        # création du html avec le javascript intégré
        my_html = f"<script>{my_js}</script>"
        js_activé = True
st.write("voici votre mot de passe sécurisé que vous pouvez copier")
st.code(mot_de_passe_gen)

# Résultat final
st.write("Merci d'avoir utilisé cette application. 🚀")

if js_activé:
    #execution du html ici pour ne pas créer un espace vide entre le bouton et le mot de passe généré
    html(my_html)