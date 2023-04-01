import sys, getopt

# ID del Chat para enviar mensaje antes de Tarjetas
chat_id = ''

#def main(argv):
def despedida(chat_id):

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
            
    import requests
    TOKEN = "5937302183:AAHxqvoy9UjAIVIMlDUp6J7ny6y3D8X9brw"
    message = f"Que Jehová te bendiga por tu sacrificio de alabanza de declarar públicamente su nombre (Hebreos 13:15). 🤟🏼"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json() # this sends the message

if __name__ == "__main__":
    despedida(sys.argv[1:])