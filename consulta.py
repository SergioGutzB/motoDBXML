from xml.dom import minidom
import xml.etree.ElementTree as ET

class mayadb:	
	cadena = ""
	select = []
	where = []
	lp, lr, lista,c = [],[],[],""
	dom = ""
	filedb = ""
	consulta = ""
	tabla = ""
	tree = ""
	root = ""


	def __init__(self,filedb):
		self.filedb=filedb;
		self.tree = ET.parse(self.filedb)
		self.root = self.tree.getroot()

	def separar(self):
		self.cadena = self.consulta.split("where")
		self.select = self.cadena[0].replace("select ","").strip()
		self.tabla = self.select[0:self.select.find("(")]
		self.select = self.select[self.select.find("(")+1:self.select.find(")")].strip().split(" ")
		self.where = self.cadena[1].strip().split(", ")
		for e in self.where:
			d = e.split("=")		
			self.lp.append(d[0])
			self.lr.append(d[1])

	def mostrar(self, root):
		self.separar()
		for i in root.iter(self.tabla):	
			for p in range(0,len(self.lp)):
				for h in i.iter():
					if (h.text == self.lr[p] and h.tag== self.lp[p]):
						for z in self.select:
							self.c+= i.find(z).text+" "
						self.c+="\n"
				if i.attrib:
					for a in i.attrib:
						if i.attrib[a]== self.lr[p] and a == self.lp[p]:
							for z in range(0,len(self.select)):
								self.c+= i.get(self.select[z])+ " | "
							self.c+="\n"
					

		print "\nEl resultado de la consulta es:"
		print "\n"
		print self.c
 
				
 
	def consultar(self):
		print "\n\nLa consulta solo debe contener espacios y las etiquetas (select, where) deben ir en minpusculas."
		print "Ejemplo: 'select integrante(nombre nacimiento instrumento) where instrumento=Guitarra, nacimiento=13 de septiembre de 1961'.\n"
		self.consulta =raw_input("Ingrese una consulta:\n")
		#self.consulta = 'select integrante(nombre nacimiento instrumento) where instrumento=Guitarra, instrumento=Bajo'

		self.mostrar(self.root)

db=mayadb("Banda.xml")
db.consultar()