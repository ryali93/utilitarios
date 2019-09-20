#!/usr/bin/env python
# -*- coding: utf-8 -*-

import win32com.client

def send_email():
     Msg = o.CreateItem(0)
    Msg.From = u"comunicacion2@ingemmet.gob.pe"
    Msg.To = u"autonomoosi02@ingemmet.gob.pe"
    Msg.Subject = u"Actualizacion del registro: Módulo de Geopedologia"
    Msg.Body = u"Hola, \n\n Se han actualizado los registros con los siguientes códigos: "
    Msg.Send()

send_email()



# SERVER = "10.102.0.48"
# FROM = u"comunicacion2@ingemmet.gob.pe"
# TO = [u"autonomoosi02@ingemmet.gob.pe"]

# SUBJECT = "Subject"
# TEXT = "Your Text"

# # Prepare actual message
# message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

# %s
# """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

# # Send the mail
# import smtplib
# server = smtplib.SMTP(SERVER, 25)
# server.login(u"comunicacion2@ingemmet.gob.pe", "comunicacion2013")
# server.sendmail(FROM, TO, message)
# server.quit()