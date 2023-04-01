# Ejemplo
# python llenarFormulario.py --chat_id "334575560" --territorio "Sangolqui" --nombre "José Ignacio Yánez" --detalles "Casa de 2 pisos al Lado de 2 terrenos baldíos. *Cuidado con el Perro* Visitar por las Noches a partir de las 10 PM" --tipoSenias "Poco Señas" --edad "23" --telefono "0983122095" --direccion "Autopista General Rumiñahui y Machachi. Urb. Navarra 1 Lote 20 Sector El Colibrí" --longitud -0.2746988 --latitud -78.4989617 --longitud -0.2746999 --latitud -78.4989627 --longitud -0.2746977 --latitud -78.4989637

import sys, getopt, datetime, os
from fillpdf import fillpdfs

def main(argv):

    # Campos Plantilla
    chat_id = ''
    territorio = ''
    nombre = ''
    detalles = ''
    tipoSenias = ''
    fechaTarjeta = ''
    edad = ''
    telefono = ''
    direccion = ''
    longitud = []
    latitud = []

    # Parse argumentos
    try:
        opts, args = getopt.getopt(argv,"hc:t:n:d:s:f:e:c:a:g:l:",["chat_id=", "territorio=", "nombre=", "detalles=", "tipoSenias=", "fechaTarjeta=", "edad=", "telefono=", "direccion=", "longitud=", "latitud="])
    except getopt.GetoptError:
        print ('Usage: python llenarFormulario.py --territorio "Sangolqui" --nombre "José Ignacio Yánez" --detalles "Casa de 2 pisos al Lado de 2 terrenos baldíos. *Cuidado con el Perro* Visitar por las Noches a partir de las 10 PM" --tipoSenias "Poco Señas" --edad "23" --telefono "0983122095" --direccion "Autopista General Rumiñahui y Machachi. Urb. Navarra 1 Lote 20 Sector El Colibrí"')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Usage: python llenarFormulario.py --territorio "Sangolqui" --nombre "José Ignacio Yánez" --detalles "Casa de 2 pisos al Lado de 2 terrenos baldíos. *Cuidado con el Perro* Visitar por las Noches a partir de las 10 PM" --tipoSenias "Poco Señas" --edad "23" --telefono "0983122095" --direccion "Autopista General Rumiñahui y Machachi. Urb. Navarra 1 Lote 20 Sector El Colibrí"')
            sys.exit()
        elif opt in ("-c", "--chat_id"):
            chat_id = arg
        elif opt in ("-t", "--territorio"):
            territorio = arg
        elif opt in ("-n", "--nombre"):
            nombre = arg
        elif opt in ("-d", "--detalles"):
            detalles = arg
        elif opt in ("-s", "--tipoSenias"):
            tipoSenias = arg
        elif opt in ("-f", "--fechaTarjeta"):
            fechaTarjeta = arg
        elif opt in ("-e", "--edad"):
            edad = arg
        elif opt in ("-t", "--telefono"):
            telefono = arg
        elif opt in ("-a", "--direccion"):
            direccion = arg
        elif opt in ("-g", "--longitud"):
            longitud.append(arg)
        elif opt in ("-l", "--latitud"):
            latitud.append(arg)
    if fechaTarjeta == '':
        fechaTarjeta = datetime.datetime.now()

    print ('Territorio es ', territorio)
    print ('Nombre es ', nombre)
    print ('Detalles es ', detalles)
    print ('TipoSenias es ', tipoSenias)
    print ('Fecha de Tarjeta es ', fechaTarjeta)
    print ('Edad es ', edad)
    print ('Telefono es ', telefono)
    print ('Direccion es ', direccion)
    print ('Longitud es ', longitud)
    print ('Latitud es ', latitud)

    # Llenar Plantilla
    datos_plantilla = {
        "territorio": territorio,
        "nombre": nombre,
        "detalles": detalles,
        "tipoSenias": tipoSenias,
        "fechaTarjeta": fechaTarjeta,
        "edad": edad,
        "telefono": telefono,
        "direccion": direccion
    }
    fillpdfs.write_fillable_pdf('./static/plantilla.pdf', 'llena.pdf', datos_plantilla)

    # Insertar imagenes y botones con PyMuPDF    
    import fitz

    archivo_entrada = "llena.pdf"
    archivo_salida = f"{nombre}.pdf"
    archivo_salida = archivo_salida.replace(" ", "_")
    googlemaps_logo = "./static/googlemaps.png"
    osmand_logo = "./static/osmand.png"

    zoom = 16

    # Imagen

    # Descarga
    import requests

    # URLs de Pines por Pixeles
    # El resto https://imgur.com/a/5iuldG9
    # https://imgur.com/a/jvxDr8f

    imgUrl = 'https://maps.googleapis.com/maps/api/staticmap?size=640x640&scale=2&center={longitud},{latitud}&zoom={zoom}&maptype=roadmap&style=feature:landscape%7Cvisibility:off&style=feature:poi%7Cvisibility:off&style=feature:poi.government%7Cvisibility:on&style=feature:poi.medical%7Cvisibility:on&style=feature:poi.park%7Cvisibility:on&style=feature:poi.place_of_worship%7Cvisibility:on&style=feature:poi.school%7Cvisibility:on&style=feature:poi.sports_complex%7Cvisibility:on&style=feature:road.arterial%7Celement:geometry.stroke%7Ccolor:0xff0000%7Cweight:1&style=feature:road.local%7Celement:geometry.stroke%7Ccolor:0x000000%7Cvisibility:on%7Cweight:0.5&markers=icon:https://i.imgur.com/q1Iqwe5.png%7Cscale:2%7C{longitud},{latitud}'.format(longitud=longitud[0], latitud=latitud[0], zoom=zoom)
    
    # Obtener numero de vecinos
    otros_sordos_asignados = len(longitud) - 1
    # Aniadir iterativamente marcadores secundarios
    for i in range(otros_sordos_asignados):
        imgUrl += f'&markers=icon:https://i.imgur.com/TE6KFO2.png%7Cscale:2%7C{longitud[i+1]},{latitud[i+1]}'
    # Aniadir key
    imgUrl += '&key=AIzaSyCOyPMMXtvhi3I5FXi9KzY-EphqVlAfGfk'

    imgData = requests.get(imgUrl).content
    with open("mapa.jpg", 'wb') as handlerImage:
        handlerImage.write(imgData)

    # Recorte
    # de 1280x1280 debe pasar a 1280x775
    from PIL import Image
    mapa = Image.open("./mapa.jpg")
    # (left, top, right, bottom)
    box = (0,252,1280,1027)
    imgCropped = mapa.crop(box)
    imgCropped.save("mapaCrop.png")
    mapa_file = "mapaCrop.png"
    leyenda_file = "./static/leyendaMapa.jpg"
    
    # Botones
    googlemaps_rectangle = fitz.Rect(150,440,215,505)
    osmand_rectangle = fitz.Rect(350,440,415,505)
    # Mapa
    mapa_rectangle = fitz.Rect(4,515,563,853)
    leyenda_rectangle = fitz.Rect(4, 828, 197, 858)

    archivo = fitz.open(archivo_entrada)
    primera_pagina = archivo[0]

    # Insertar en PDF
    primera_pagina.insert_image(googlemaps_rectangle, filename=googlemaps_logo)
    primera_pagina.insert_image(osmand_rectangle, filename=osmand_logo)
    primera_pagina.insert_image(mapa_rectangle, filename=mapa_file)
    primera_pagina.insert_image(leyenda_rectangle, filename=leyenda_file)
    primera_pagina.insert_link({'kind': 2, 'from': googlemaps_rectangle, 'uri': f'https://www.google.com/maps/search/?api=1&query={longitud[0]},{latitud[0]}'})
    primera_pagina.insert_link({'kind': 2, 'from': osmand_rectangle, 'uri': f'https://osmand.net/map?pin={longitud[0]},{latitud[0]}#16/{longitud[0]}/{latitud[0]}'})    
    archivo.save(archivo_salida)

    # Delete temp files
    os.remove("llena.pdf")
    os.remove("mapa.jpg")
    os.remove("mapaCrop.png")

    # Compress
    # https://github.com/pts/pdfsizeopt
    try:
        print("Comprimiendo...")
        os.system(f'docker run -v "$PWD:/workdir" -u "$(id -u):$(id -g)" --rm -it ptspts/pdfsizeopt pdfsizeopt --use-pngout=no {archivo_salida} {archivo_salida} >/dev/null 2>&1')
        print("Comprimido")
    except:
        print("Error al comprimir")


    # Send Saludo
    print("Saludando...")
    from telegramSaludo import saludar
    saludar(chat_id)


    # Send Document

    import requests

    token = "5937302183:AAHxqvoy9UjAIVIMlDUp6J7ny6y3D8X9brw"

    files = {'document': open(f'{archivo_salida}', 'rb')}

    resp = requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={chat_id}', files=files)

    if resp.status_code == 200:
        print(resp.status_code , " The document was sent succesfully")
    else:
        print(resp.status_code , " The document was not sent")

    # Send Despedida
    print("Despidiendo...")
    from telegramDespedida import despedida
    despedida(chat_id)


if __name__ == "__main__":
    main(sys.argv[1:])

# https://github.com/pymupdf/PyMuPDF/issues/283
