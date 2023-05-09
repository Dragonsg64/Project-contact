import sqlite3
import sys
import re
format_tel = "[0][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
format_email = "^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"
con = sqlite3.connect("contact.db")
cur = con.cursor()


def nouveau(Nom, Prénom, Surnom, Téléphone, Email, Adresse_postale):
    try:
        new_contact ='''INSERT INTO contacts VALUES(?, ?, ?, ?, ?, ?)'''
        insert = (Nom, Prénom, Surnom, Téléphone, Email, Adresse_postale)
        cur.execute(new_contact, insert)
        con.commit()
        cur.close
        con.close
    except sqlite3.Error as error:
        print("Erreur lors de l'ajout du contact !", error)

def supprimer(Nom, Prénom, Surnom, Téléphone, Email, Adresse_postale):
    try:
        suppr ='''DELETE FROM contacts WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone = ? AND Email = ? AND Adresse_postale = ?'''
        insert = (Nom, Prénom, Surnom, Téléphone, Email, Adresse_postale)
        cur.execute(suppr, insert)
        con.commit()
        cur.close()
        con.close()
    except sqlite3.Error as error:
        print("Erreur lors du suppression du contact", error)

def liste():
    try:
        afficher ='''SELECT * FROM contacts'''
        result = cur.execute(afficher).fetchall()
        print(result)
        con.commit()
        cur.close()
        con.close()
    except sqlite3.Error as error:
        print("Erreur lors de l'affichage !", error)

def search(zone, rechercher):
    try:
        if zone == "Nom":
            select = '''SELECT * from Contacts WHERE Nom = ?'''
        if zone == "Prénom":
            select = '''SELECT * from Contacts WHERE Prénom = ?'''
        if zone == "Surnom":
            select = '''SELECT * from Contacts WHERE Surnom = ?'''
        if zone == "Téléphone":
            select = '''SELECT * from Contacts WHERE Téléphone = ?'''
        if zone == "Email":
            select = '''SELECT * from Contacts WHERE Email = ?'''
        if zone == "Adresse_postale":
            select = '''SELECT * from Contacts WHERE Adresse_postale = ?'''
        utile = (rechercher, )
        result = cur.execute(select, utile)
        result = cur.fetchall()
        print(result)
        con.commit()
        cur.close()
        con.close()
    except sqlite3.Error as error:
        print("Erreur lors de la recherche !", error)

def MAJ(Loca_update,New_data,Nom, Prenom, Surnom, Téléphone, Email, Adresse_postale):
    if Loca_update == "Nom":
        Cmd ='''UPDATE Contacts SET Nom = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse_postale=? '''
    if Loca_update == "Prénom":
        Cmd ='''UPDATE Contacts SET Prénom = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse_postale=? '''
    if Loca_update == "Surnom":
        Cmd ='''UPDATE Contacts SET Surnom = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse_postale=? '''
    if Loca_update == "Téléphone":
        Cmd ='''UPDATE Contacts SET Téléphone = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse_postale=? '''
    if Loca_update == "Email":
        Cmd ='''UPDATE Contacts SET Email = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse_postale=? '''
    if Loca_update == "Adresse_postale":
        Cmd ='''UPDATE Contacts SET Adresse_postale = ? WHERE Nom = ? AND Prénom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse_postale=? '''
    try:
        Update = (New_data,Nom, Prenom, Surnom, Téléphone, Email, Adresse_postale)
        cur.execute(Cmd, Update)
        con.commit()
        cur.close()
        con.close()  
    except sqlite3.Error as error:
        print("Erreur lors de la mise à jour ! ", error)

def aide():
    print("bonjour a toi")
    print("voici les commandes que tu peux utilisé pour gérer ta liste de contact")
    print("\n")
    print("Quand tu veux faire une commande il faut toujour commencer par 'python3 contact.py' ensuite voici ce qu'il faut ajouter a la suite")
    print("l'option new sert on ajoute des nouveaux contacts dans notre liste")
    print("l'option delete sert on supprime les contacts de notre liste")
    print("l'option list sert a afficher la liste de ces contacts")
    print("l'option search --by-phone 'numéro de téléphone' permet de rechercher un contact en fonction de son numéro de téléphone")
    print("l'option search --by-name 'nom' permet de rechercher un contact en fonction de son nom de famille")
    print("l'option search --by-email 'email' permet de rechercher un contact en fonction de son adresse email")
    print("l'option search --by-address 'adresse_postale' permet de rechercher un contact en fonction de son adresse postale")
    print("l'option search --by-nickname 'surnom' permet de rechercher un contact en fonction de son surnom")
    print("l'option search --by-firstname 'prénom' permet de rechercher un contact en fonction de son prénom")

def intéract():
    choix = None
    print("Bienvenue dans en mode intéractif")
    while choix != "au revoir":
        print("Tapez 1 pour ajouter un contact ")
        print("Tapez 2 pour supprimer un contact ")
        print("Tapez 3 pour voir vos contacts ")
        print("Tapez 4 pour rechercher un ou plusieurs contacts ")
        print("Tapez 5 pour modifier un contact ")
        print("Tapez 6 pour de l'aide ")
        choix = input("Que voulez vous faire ? : ")
        if choix == "1":
            Nom= input('Quel est le nom de votre contact : ')
            Prenom= input('Quel est le prénom de votre contact : ')
            Surnom= input('Quel est le surnom de votre contact : ')
            Telephone= input('Quel est le numéro de téléphone de votre contact : ')
            Email = input('Quel est le mail de votre contact : ')
            Adresse_postale= input("Quel est l'adresse_postale de votre contact : ")
            nouveau(Nom,Prenom,Surnom,Telephone,Email,Adresse_postale)
            print("ajout du contact réussie")
            print("\n")
            print("\n")
        if choix =="2":
            Nom= input('Quel est le nom de votre contact a supprimer : ')
            Prenom= input('Quel est le prénom de votre contact a supprimer : ')
            Surnom= input('Quel est le surnom de votre contact a supprimer : ')
            Telephone= input('Quel est le numéro de téléphone de votre contact a supprimer : ')
            Email= input('Quel est le mail de votre contact a supprimer : ')
            Adresse_postale= input("Quel est l'adresse de votre contact a supprimer : ")
            supprimer(Nom,Prenom,Surnom,Telephone,Email,Adresse_postale)
            print("Suppression réussie")
            print("\n")
            print("\n")      
        if choix == "3":    
            liste()   
            print("\n")
            print("\n")
        if choix == "4":
            zone = input("Quel est la zone de recherche (Nom/Prénom/Surnom/Téléphone/Email/Adresse_postale) : ")
            rechercher = input("Tu recherche qui ?")
            search(zone, rechercher) 
            print("\n")
            print("\n")
        if choix =="5":
            Loca_update = input("Quel est la colonne a modifier (Nom/Prénom/Surnom/Téléphone/Email/Adresse_postale): ")
            New_data = input("Quel est la nouvelle donnée : ")
            Nom= input('Quel est le nom de votre a mettre a jour : :')
            Prenom= input('Quel est le prénom de votre contact a mettre a jour :')
            Surnom= input('Quel est le surnom de votre contact a mettre a jour :')
            Telephone= input('Quel est le numéro de téléphone de votre contact a mettre a jour : ')
            Email= input('Quel est le mail de votre contact a mettre a jour : ')
            Adresse_postale= input("Quel est l'adresse de votre contact a mettre a jour : ")
            MAJ(Loca_update, New_data, Nom, Prenom, Surnom, Telephone, Email, Adresse_postale)
            print("\n")
            print("\n")
        if choix =="6":
            aide()
            print("\n")
            print("\n")

for arg in sys.argv:
        try:
            if sys.argv[1] == "new":
                Nom = input("Quel est le nom:")
                Prénom = input("Quel est le prénom:")
                Surnom = input("Quel est le Surnom:")
                Téléphone = input("Quel est le numéro Téléphone:")
                Email = input("Quel est l'Email:")
                Adresse_postale = input("Quel est l'adresse postale:")
                nouveau(Nom, Prénom, Surnom, Téléphone, Email, Adresse_postale)
                print("le nouveau contact a été ajouter")
                break
            if sys.argv[1] == "delete":
                Nom= input("Quel est le nom:")
                Prénom= input("Quel est le prénom:")
                Surnom = input("Quel est le Surnom:")
                Téléphone = input("Quel est le numéro Téléphone:")
                Email = input("Quel est l'Email:")
                Adresse_postale = input("Quel est l'adresse postale:")
                supprimer(Nom, Prénom, Surnom, Téléphone, Email, Adresse_postale)
                print("le contact a été supprimer")
                break
            if sys.argv[1] == "list":
                liste()
                break
            if sys.argv[1] == "search":
                rechercher = sys.argv[3]
                try:
                    if sys.argv[2] == "--by-name" :
                        zone = "Nom"
                    if sys.argv[2] == "--by-tel" :
                        zone = "Téléphone"
                    if sys.argv[2] == "--by-email" :
                        zone = "Email"
                    if sys.argv[2] == "--by-nickname" :
                        zone = "Surnom"
                    if sys.argv[2] == "--by-firstname" :
                        zone = "Prénom"
                    if sys.argv[2] == "--by-address" :
                        zone = "Adresse"
                    search(zone, rechercher)
                    break
                except:
                        print ("Veuillez respecter les commandes ou veuillez entrer dans le mode intéractif ")
                break
            if sys.argv[1] == "update":
                Loca_update = input("Quel est la colonne a modifier (Nom/Prénom/Surnom/Téléphone/Email/Adresse_postale): ")
                New_data = input("Quel est la nouvelle donnée : ")
                Nom= input('Quel est le nom de votre a mettre a jour : :')
                Prenom= input('Quel est le prénom de votre contact a mettre a jour :')
                Surnom= input('Quel est le surnom de votre contact a mettre a jour :')
                Telephone= input('Quel est le numéro de téléphone de votre contact a mettre a jour : ')
                Email= input('Quel est le mail de votre contact a mettre a jour : ')
                Adresse_postale= input("Quel est l'adresse de votre contact a mettre a jour : ")
                MAJ(Loca_update, New_data, Nom, Prenom, Surnom, Telephone, Email, Adresse_postale)
                break
            if sys.argv[1] == "?":
                aide()
                break
        except:
            intéract()