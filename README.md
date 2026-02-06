# La Bayeta de la Fortuna

Aplicación web que proporciona frases auspiciosas aleatorias, al estilo de las galletas de la fortuna o servilletas de bar.

## Descripción
Cada vez que accedes a la web, recibirás un mensaje inspirador o auspicioso diferente.

## Tecnologías
- Python
- Git
- Docker

## Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone git@github.com:Javiier1/pps_python_git_docker.git
cd pps_python_git_docker
```

### 2. Crear y activar entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate  # En Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python app.py
```

### 5. Desactivar el entorno virtual (cuando termines)
```bash
deactivate
```

## API Endpoints

### GET /
Página de bienvenida

### GET /frotar/<n_frases>
Obtiene N frases auspiciosas aleatorias

**Ejemplo:**
```bash
curl http://localhost:5000/frotar/5
```

**Respuesta:**
```json
{
  "frases": [
    "Hoy será un gran día lleno de oportunidades",
    "La fortuna sonríe a los valientes",
    "Tus esfuerzos pronto darán frutos"
  ]
}
```

## Despliegue con Docker

### Construir imagen
```bash
docker build -t bayeta-fortuna .
```

### Ejecutar contenedor
```bash
docker run -d -p 5000:5000 --name bayeta-app bayeta-fortuna
```

### Acceder a la aplicación
http://localhost:5000

### Parar contenedor
```bash
docker stop bayeta-app
docker rm bayeta-app
```
