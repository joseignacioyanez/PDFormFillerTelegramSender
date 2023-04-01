import sys, getopt

# ID del Chat para enviar mensaje antes de Tarjetas
chat_id = ''

#def saludar(argv):
def saludar(chat_id):
    
    '''
    # Parse argumentos
    try:
        opts, args = getopt.getopt(argv,"hc:",["chat_id="])
    except getopt.GetoptError:
        print ('Usage: python telegramSaludo.py --chat_id "334575560"')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Usage: python telegramSaludo.py --chat_id "334575560"')
            sys.exit()
        elif opt in ("-c", "--chat_id="):
            chat_id = arg
    '''


    # Fecha actual con formato
    import datetime

    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

    hoy = datetime.datetime.now()
    hoy_texto = ""
    hoy_texto += dias[int(hoy.strftime("%w"))]
    hoy_texto += ", "
    hoy_texto += hoy.strftime("%d")
    hoy_texto += " de "
    hoy_texto += meses[int(hoy.strftime("%m")) - 1]
    hoy_texto += " del "
    hoy_texto += hoy.strftime("%Y")

    import requests
    TOKEN = "5937302183:AAHxqvoy9UjAIVIMlDUp6J7ny6y3D8X9brw"
    message = f"🙋🏻‍♂️🙋🏻‍♀️ ¡Saludos!\nEstas son las tarjetas de territorio que se le han asignado:\n\n{hoy_texto}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json() # this sends the message

if __name__ == "__main__":
    saludar(sys.argv[1:])