from outils import *
class ConfigModule:
	def __init__(self,endroit):
		self.endroit = endroit + "configModule.f"
		self.openConfig()

	def initialisation(self):
		# Initialise les variables
		self.nom = ""
		self.arduino = False
		self.ressourceAudio = False
		self.versionFRMC = ""


	def setNom(self,nom):
		# Fonction permettant de modifier le nom du module dans le fichier de config
		self.nom= nom
		self.save()

	def setVersionFRMC(self,valeur):
		# Fonction permettant de modifier la version du FReveilModuleCreator
		self.versionFRMC= valeur
		self.save()

	def setArduino(self,arduino):
		self.arduino = arduino
		self.save()

	def setRessourceAudio(self,ressourceAudio):
		self.ressourceAudio = ressourceAudio
		self.save()


	def save (self):
		# Sauvegarde du fichier
		chaine = Outils.constitueBalise("Nom",str(self.nom)) + "\n" + Outils.constitueBalise("Arduino",str(self.arduino)) + "\n" 
		chaine += Outils.constitueBalise("RessourceAudio",str(self.ressourceAudio)) + "\n"+ Outils.constitueBalise("VersionFMRC",str(self.versionFRMC))+"\n"
		Outils.ecrireFichier(self.endroit,chaine)

	def openConfig(self):
		# Permet d'ouvrir la configuration si elle existe
		self.initialisation()
		if (Outils.testPresence(self.endroit)):
			chaine = Outils.lireFichier(self.endroit)
			self.arduino = Outils.recupereBaliseAuto(chaine, "Arduino", 1, "Arduino") == "True"
			self.ressourceAudio = Outils.recupereBaliseAuto(chaine, "RessourceAudio", 1) == "True"
			self.nom =Outils.recupereBaliseAuto(chaine,"Nom",1)
			self.versionFRMC =Outils.recupereBaliseAuto(chaine,"VersionFMRC",1)
			

