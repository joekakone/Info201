#! usr/bin/env python
# *-* coding : utf-8 *-*

import sqlite3

from fonctions_elementaires import *


def get_all():
	connection = sqlite3.connect("base_notes.db")
	curseur = connection.cursor()

	req = curseur.execute("SELECT * FROM ues")

	print("LISTE DES UNITES D'ENSEIGNEMEMT")
	#print("ID\tCODE\tLIBELLE\tNOMBRES DE CREDITS")
	for ue in req.fetchall():
		print(ue)

	connection.close()

def get_one():
	connection = sqlite3.connect("base_notes.db")
	curseur = connection.cursor()
	
	id_ = saisir_id()

	#print("ID SAISI: ", id, type(id))
	req = curseur.execute("SELECT * FROM ues WHERE (id_ue = {})".format(id_))
	print("Resultat: ", req.fetchone())

	connection.close()

def post():
	connection = sqlite3.connect("base_notes.db")
	curseur = connection.cursor()

	ue_ = saisir_ue()

	try:
		req = curseur.execute("INSERT INTO ues (code_ue, libelle_ue, credit_ue) VALUES {}".format(ue_))
		connection.commit()
	except Exception as e:
		print("ERREUR D'ENREGISTREMENT: ", e)
	
	connection.close()
	
def update():
	pass

def delete():
	pass

