import streamlit as st
import pandas as pd
import random

# Titre et sous-titre
st.title("Application Web avec Streamlit")
st.subheader("Découverte des fonctionnalités de Streamlit")

# Texte d'introduction
st.write("Bienvenue sur cette application interactive réalisée avec Streamlit. Explorez les différents composants ci-dessous.")

# Ajout d'une image
st.image("image.png", caption="Image d'exemple")

score = 0
mot_de_passe_longeur = False
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
long = 12
max = False

def generer_mot_de_passe(longueur=12, majuscules=True,
minuscules=True, chiffres=True, speciaux=True):

    caracteres = ""
    if majuscules:
        caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if minuscules:
        caracteres += "abcdefghijklmnopqrstuvwxyz"
    if chiffres:
        caracteres += "0123456789"
    if speciaux:
        caracteres += "!@#$%^&*()-_+=<>?/"
    if not caracteres:
        return "Sélectionnez au moins un type de caractère."
    return "".join(random.choice(caracteres) for _ in
    range(longueur))


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
if st.button("verrifier mon mot de passe"):
    button_cliqué = True
    score_mdp()
if score > 10 :
    score = 10
# Curseur interactif
valeur_curseur = st.slider("score de votre mot de passe :", 0, 10, score, disabled=True)
st.write(f"Score de votre mot de passe : {valeur_curseur}")

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
long = st.text_input("Entrez le nombre de caractères souhaités :", "")
long =  int(long)
if maj and min and spe and num and long >= 12 :
    max = True
if st.button("générer un mot de passe") :
    mot_de_passe = (generer_mot_de_passe(long, maj, min, num, spe))
while max and score < 10 :
    if max :
        score_mdp()
    if score < 10 :
        mot_de_passe = (generer_mot_de_passe(long, maj, min, num, spe))

st.write(mot_de_passe)
    

# Résultat final
st.write("Merci d'avoir utilisé cette application. 🚀")
