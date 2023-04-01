# python llenarFormulario.py 
# --chat_id "334575560" 
# --territorio "Sangolqui" 
# --nombre "José Ignacio Yánez" 
# --detalles "Casa de 2 pisos al Lado de 2 terrenos baldíos. *Cuidado con el Perro* Visitar por las Noches a partir de las 10 PM" 
# --tipoSenias "Poco Señas" 
# --edad "23" 
# --telefono "0983122095" 
# --direccion "Autopista General Rumiñahui y Machachi. Urb. Navarra 1 Lote 20 Sector El Colibrí" 
# --longitud -0.2746988 
# --latitud -78.4989617 
# --longitud -0.2746999 
# --latitud -78.4989627 
# --longitud -0.2746977 
# --latitud -78.4989637

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/fillForm', methods=['POST'])
def fillForm():
    try:
        # Parse the JSON data from the request body
        data = request.get_json()

        print(data)

        # Extract the parameters from the JSON object
        chat_id = data['chat_id']
        territorio = data['territorio']
        nombre = data['nombre']
        detalles = data['detalles']
        tipoSenias = data['tipoSenias']
        edad = data['edad']
        telefono = data['telefono']
        direccion = data['direccion']
        # Extract JSON arrays of coordinates      
        longitud = data['longitud']
        latitud = data['latitud']

        print(longitud[0])
        print(longitud[1])
        print(latitud)

        command = f'python llenarFormulario.py  -c "{chat_id}" -t "{territorio}" -n "{nombre}" --detalles "{detalles}" --tipoSenias "{tipoSenias}" --edad "{edad}" --telefono "{telefono}" --direccion "{direccion}" '

        coordenadasString = ''
        numeroDeCoordenadas = len(longitud)
        for i in range(numeroDeCoordenadas):
            command += f' --longitud "{longitud[i]}" --latitud "{latitud[i]}" '

        print(command)

        os.system(command)

        # Return the result as a JSON object
        return jsonify({'result': "yes"})
    except Exception as e:
        # Log the error message and return a 500 error response
        app.logger.error(e)
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)