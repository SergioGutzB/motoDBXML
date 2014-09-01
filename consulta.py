from xml.dom import minidom

class mayadb:	
	cadena = ""
	select = []
	where = []
	lp, lr, lista,c = [],[],[],""
	dom = ""
	filedb = ""
	consulta = ""

	def __init__(self,filedb):
		self.filedb=filedb;
		self.dom = minidom.parse(self.filedb)

	def separar(self):
		self.cadena = self.consulta.split("where")
		self.select = self.cadena[0].replace("select ","").strip().split(" ")
		self.where = self.cadena[1].strip().split(" ")

	def ejecutar(self):		
		self.separar()
		for e in self.where:
			d = e.split("=")		
			self.lp.append(d[0])
			self.lr.append(d[1])		

		for i in range(0,len(self.lp)):			
			re = self.dom.getElementsByTagName(self.lp[i])
			for j in range(0,len(re)):
				if re[j].childNodes[0].nodeValue == self.lr[i]:
					self.c+="\n"
					for h in range(0,len(self.select)):
						elements = self.dom.getElementsByTagName(self.select[h])
						self.c+= elements[j].childNodes[0].nodeValue + " "		
		print self.c + "\n"

	def consultar(self):
		print "\nLa consulta solo debe contener espacios y las etiquetas (select, where) deben ir en minpusculas."
		print "Ejemplo: 'select nombre nacionalidad sitio_web ano where ano=1983 ano=1982'.\n"
		self.consulta =raw_input("Ingrese una consulta:\n")
		self.ejecutar()
		

db=mayadb("Banda.xml")
db.consultar()