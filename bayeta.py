import random

def frotar(n_frases: int = 1) -> list:
    """
    Devuelve una lista con n_frases aleatorias del archivo frases.txt
    """
    try:
        with open('frases.txt', 'r', encoding='utf-8') as f:
            todas_las_frases = [linea.strip() for linea in f if linea.strip()]
        
        # Si se piden más frases de las que hay, podemos repetir
        if n_frases > len(todas_las_frases):
            return random.choices(todas_las_frases, k=n_frases)
        else:
            return random.sample(todas_las_frases, k=n_frases)
    except FileNotFoundError:
        return ["Error: No se encontró el archivo de frases"]
