import imghdr
import os
import smtplib
from email.message import EmailMessage
import csv
from fpdf import FPDF

EMAIL_ADDRESS= os.environ.get('EMAIL_USER')
EMAIL_PASSWORD= os.environ.get('EMAIL_PASS')

with open ("DatosReporte.csv", encoding='utf-8')as File:
    reader= csv.reader(File,delimiter=',', quoting=csv.QUOTE_MINIMAL)
    maestra = list(reader)

    
for empleado in maestra [1:]:

	Correo= empleado[2]
	Apellido= empleado[1]
	Nombre=empleado[0]


	pdf_personalizado= FPDF()
	pdf_personalizado.add_page()
	pdf_personalizado.set_font("Arial", size=25)
	pdf_personalizado.cell(200, 10, txt=Nombre, ln=1)
	text= "Hola! este es un mensje de prueba\n para revisar que cada quien\n reciva su propio PDF"
	pdf_personalizado.cell(200, 10, txt=text, ln=1)
	pdf_personalizado.output("PDF_personalizado.pdf")

	msg= EmailMessage()
	msg['Subject'] = 'Mensaje de los Lunes'
	msg['From']= EMAIL_ADDRESS
	msg['To']= Correo
	msg.set_content('Este es el correo que llega todos los lunes')

	files = ['PDF_personalizado.pdf']

	for file in files:
		with open (file, 'rb') as f:
			file_data = f.read()
			file_name = f.name
		  
		
	    

		msg.add_attachment(file_data, maintype='application', subtype='octet_stream', filename=file_name)

		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
			smtp.send_message(msg)
			print(Correo)
			print(Nombre)




	


	
	

	    










