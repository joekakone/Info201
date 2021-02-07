#! usr/bin/env python
# *-* coding : utf-8 *-*

UES = ["ANG", "INF", "MTH", "PHY"]

LONGUEURCODEUE = 6
NOMBRES = [2, 3, 4]

INDICEMIN = 1
INDICEMAX = 6


def choix_menu():
	try:
		choix = input("CHOIX: ")
		choix = int(choix)
		assert not ((choix < INDICEMIN) or (choix > INDICEMAX))
	except AssertionError:
		print("CHOIX INCORRECT")
		choix = 0
	except Exception:
		print("SAISIE INVALIDE ")
		choix = 0
	return choix

def menu():
	print("===================")
	print("======M-E-N-U======")
	print("===================")
	print("1-GET ALL")
	print("2-GET ONE")
	print("3-POST")
	print("4-UPDATE")
	print("5-DELETE")
	print("6-RESET")
	print("===================")

	choix = 0
	while choix == 0:
		choix = choix_menu()
		if choix != 0:
			break

	return choix

def saisir_id():
	while True:
		try:
			id_ = input("SAISIR L'ID DE L'UE: ")
			id_ = int(id_)
			assert id_ >= 1
			break
		except AssertionError:
			print("IDENTIFIANT INCOREECT")
			continue
		except Exception as e:
			raise print("SAISIE INVALIDE")

	return id_

def saisir_code():
	while True:
		try:
			code_ = input("CODE DE l'UE: ")
			code_ = code_.replace(" ", "")
			code_ = code_.upper()

			if len(code_) != LONGUEURCODEUE:
				print("CODE INCORRECT")
				continue
			else:
				code_lettre = code_[:3]
				code_chiffre = int(code_[3:])
				if (code_lettre not in UES) or (code_chiffre < 100 or code_chiffre >= 400):
					print("CODE INCORRECT")
					continue
				else:
					break
		except Exception as e:
			print("SAISIE INVALIDE ")

	return code_

def saisir_libelle():
	while True:
		libelle_ = input("LIBELLE DE L'UE: ")
		if len(libelle_) > 0:
			break
	return libelle_

def saisir_credit():
	while True:
		try:
			credit_ = input("NOMBRE DE CREDITS: ")
			credit_ = int(credit_)
			assert credit_ in NOMBRES
			break
		except Exception as e:
			print("SAISIE INVALIDE")
		except AssertionError:
			print("NOMBRE INCORRECT")
	return credit_

def saisir_ue():
	'''On doit saisir le code le libellé et le nombre de crédits 
	'''
	code_ = saisir_code()

	libelle_ = saisir_libelle()

	credit_ = saisir_credit()

	return (code_, libelle_, credit_)

