from flask import Flask, jsonify, request
from bayeta import frotar, agregar_frases

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola, mundo"

@app.route('/frotar/<int:n_frases>')
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases": frases})

@app.route('/frotar/add', methods=['POST'])
def añadir_frases():
    """
    Endpoint para añadir nuevas frases
    Espera un JSON: {"frases": ["frase1", "frase2", ...]}
    """
    try:
        data = request.get_json()
        
        if not data or 'frases' not in data:
            return jsonify({
                "error": "Formato incorrecto. Se espera: {'frases': ['frase1', 'frase2']}"
            }), 400
        
        frases_nuevas = data['frases']
        
        if not isinstance(frases_nuevas, list):
            return jsonify({
                "error": "El campo 'frases' debe ser una lista"
            }), 400
        
        resultado = agregar_frases(frases_nuevas)
        
        if resultado.get('estado') == 'ok':
            return jsonify({
                "mensaje": "Frases añadidas correctamente",
                "insertadas": resultado['insertadas']
            }), 200
        else:
            return jsonify({
                "error": resultado.get('error')
            }), 500
            
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
