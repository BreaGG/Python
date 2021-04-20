def pedirNombre():
    nombre = input("Introduzca su nombre: ")
    validacion=True
    if len(nombre) < 3:
        validacion=False
    return validacion


def pedirApellido():
    apellido = input("Introduzca su primer apellido: ")
    validacion=True
    if len(apellido) < 3:
        validacion=False
    return validacion

def pedirCorreo():
    correo = input("Introduzca su correo: ")
    validacion=True
    if not "@" in correo and len(correo) > 8 :
        validacion=False
    return validacion
 
def pedirFecha():
    fecha = int(input("Introduzca su año de nacimiento: "))
    validacion=True
    if fecha < 1900 or fecha > 2020:
        validacion=False
    return validacion

def validarNombre():
    nombre = input("Introduzca su nombre: ")
    while len(nombre) < 3:
        nombre = input("Error encontrado, introduzca su nombre correctamente: ")

def validarApellido():
    apellido = input("Introduzca su primer apellido: ")
    while len(apellido) < 3:
        apellido = input("Error encontrado, introduzca su apellido correctamente: ")

def validarEmail():
    correo = input("Introduzca su correo: ")
    while not "@" in correo and len(correo) > 8 :
        correo = input("Error encontrado, introduzca su email correctamente: ")
        
def validarFechaNac():
    fecha = int(input("Introduzca su año de nacimiento: "))
    while fecha < 1900 or fecha > 2020:
        fecha = int(input("Error encontrado, introduzca su año de nacimiento correctamente: "))   

### Programa principal
repetirPrograma=1
while repetirPrograma ==1:
    contadorErrores=0
    validNombre = pedirNombre()
    validApellido = pedirApellido()
    validCorreo = pedirCorreo()
    validFechaNac = pedirFecha()
    if validNombre == False:
        contadorErrores=contadorErrores+1
    if validApellido == False:
        contadorErrores=contadorErrores+1
    if validCorreo == False:
        contadorErrores=contadorErrores+1
    if validFechaNac == False:
        contadorErrores=contadorErrores+1
    if contadorErrores>0:
        print("Se han encontrado "+str(contadorErrores)+" errores.")
        if validNombre == False:
            validarNombre()
        if validApellido == False:
            validarApellido()
        if validCorreo == False:
            validarEmail()
        if validFechaNac == False:
            validarFechaNac()
    else:
        print("La validación ha sido correcta.")   
    repetirPrograma = int(input("¿Quieres introducir los datos de otra persona? Si: 1 | No: 2"))
    if repetirPrograma !=1:
        print("Gracias por usar el programa!")
        break
        
