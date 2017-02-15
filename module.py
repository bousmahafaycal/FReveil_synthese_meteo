"""
Ce module devra par la suite etre importer dans le FReveil 
Module créé le : 2017_2_15
Nom initial du module : synthese_meteo

"""
from config import *
import urllib
from outils import *
import platform
from synthese import *


def start(arguments):
	# Cette fonction sera la fonction qui sera lancée par le module. argument est une liste contenant les arguments passés au lancement du module
	
	# Le code qui suit jusqu'à #FIN est un code pour recuperer l'exclusivité pour utiliser l'audio au sein du FReveil.
	# Il suffit d'insérer votre code utilisant l'audio à l'endroit indiquer.
	# A chaque fois que vous souhaitez utiliser l'audio vous devriez utiliser ce code :

	#id = requestAudio()
	

	#giveRequestAudio(id)

	#FIN
	a = Synthese()
	a.synthese(meteo()) 


def giveRequestAudio(id):
	# Lache l'autorisation d'utiliser l'audio pour qu'un autre module puisse l'utiliser.
	conf = Config ()
	conf.setLockAudio(False,id)

def requestAudio(): 
	# Demande l'autoristion d'utiliser l'audio. Cette méthode est bloquante jusqu'à ce que l'autorisation soit donnée.
	conf = Config ()
	id = conf.getId()
	audio =  0
	while audio != 1:
		audio = conf.setLockAudio(True,id)
	return id

def meteo ():
    #Telecharger le fichier
    url = "http://www.msn.com/fr-fr/meteo?wealocations=wc:2575&q=Bagnolet%2C+Seine-Saint-Denis"
    liste_python = platform.python_version_tuple()

    if liste_python[0] == "2": # Sous python 2
        htmls = urllib.urlopen(url).read()
        chaine = str(htmls)

    if liste_python[0] == "3": # Sous python 3
        from urllib.request import urlopen
        htmls = urlopen(url).read()
        chaine = str(htmls)

    #Traitement du fichier
    debut = chaine.find ("t\" aria-label=\"")
    selection = chaine[debut+ 15 :]
    fin =  selection.find ("\"")
    chaine_final = selection[:fin]

    #Gestion des caracteres speciaux
    chaine_final = chaine_final.replace("&#233;","é")
    chaine_final = chaine_final.replace("&#232;","è")
    chaine_final = chaine_final.replace("&#160;"," ")

    #synthese(chaine_final) # On renvoie la chaine que l'on a récuperer
    return chaine_final