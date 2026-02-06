from mongo_handler import consultar_frases_aleatorias, insertar_frases, inicializar_frases

def frotar(n_frases: int = 1) -> list:
    """
    Devuelve una lista con n_frases aleatorias de MongoDB
    """
    try:
        # Inicializar si es necesario
        inicializar_frases()
        
        # Obtener frases de MongoDB
        frases = consultar_frases_aleatorias(n_frases)
        return frases if frases else ["No hay frases disponibles"]
    except Exception as e:
        return [f"Error al obtener frases: {str(e)}"]

def agregar_frases(frases_lista):
    """
    Añade nuevas frases a la base de datos
    """
    try:
        count = insertar_frases(frases_lista)
        return {"insertadas": count, "estado": "ok"}
    except Exception as e:
        return {"error": str(e), "estado": "error"}
