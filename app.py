import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

# Titre et sous-titre
st.title("Application Web avec Streamlit")
st.subheader("Découverte des fonctionnalités de Streamlit")

# Texte d'introduction
st.write("Bienvenue sur cette application interactive réalisée avec Streamlit. Explorez les différents composants ci-dessous.")

# Ajout d'une image
st.image("https://via.placeholder.com/800x300.png?text=Image+d'exemple", caption="Image d'exemple")

file  = open("mots_interdits.txt","r",encoding="utf8")
lignes = file.readlines()

# Zone de saisie
mot_de_passe = st.text_input("Entrez votre mot de passe :", "")
score = 0
mot_de_passe_longeur = False
scoremaj = False
scoremin = False
scorenum = False
scorecaractère = False
mots_interdits = False
caractères = ["!", "@", "#",  "$", "%", "^", "&", "*", "(", ")"," ?", ";"]
button_cliqué = False

# Boutons interactifs
if st.button("verrifier mon mot de passe"):
    button_cliqué = True
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


# Résultat final
st.write("Merci d'avoir utilisé cette application. 🚀")
