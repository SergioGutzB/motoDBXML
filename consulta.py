from xml.dom import minidom

def consulta(consulta):
	cadena = consulta.split("where")
	select = cadena[0].replace("select ","").strip().split(" ")
	where = cadena[1].strip().split(" ")
	lp, lr, lista,c = [],[],[],""
	dom = minidom.parse("Banda.xml")

	for e in where:
		d = e.split("=")		
		lp.append(d[0])
		lr.append(d[1])		

	for i in range(0,len(lp)):			
		re = dom.getElementsByTagName(lp[i])
		for j in range(0,len(re)):
			if re[j].childNodes[0].nodeValue == lr[i]:
				c+="\n"
				for h in range(0,len(select)):
					elements = dom.getElementsByTagName(select[h])
					c+= elements[j].childNodes[0].nodeValue + " "		
	print c + "\n"

def consultar():
	print "\nLa consulta solo debe contener espacios y las etiquetas (select, where) deben ir en minpusculas."
	print "Ejemplo: 'select nombre nacionalidad sitio_web ano where ano=1983 ano=1982'.\n"
	clta =raw_input("Ingrese una consulta:\n")
		
	consulta (clta)

consultar()		
