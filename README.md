# El Viaje Profesional 🎬

**Noticiero / Programa de Entrevistas**
- **Institución:** TdeA Aburrá Sur
- **Programa:** Técnica Profesional en Sistemas
- **Integrantes:** Ana Sofía Vallejo Henao y Juan Diego Romero
- **Tema:** EduConecta Aburrá Sur - Solución tecnológica para la brecha digital

## 📺 Descripción del Proyecto

"El Viaje Profesional" es un video noticiero que narra el recorrido de dos estudiantes a través de 4 estaciones fundamentales en su formación como profesionales en Ingeniería de Sistemas:

1. **🟢 Estación 1 - Formación Integral**: ¿Qué significa ser un profesional integral?
2. **🔵 Estación 2 - Competencias en Acción**: ¿Qué competencias necesitas para el problema?
3. **🟢 Estación 3 - Ruta Académica**: ¿Qué opción de grado y semilleros elegir?
4. **🔵 Estación 4 - Impacto Social**: ¿Cómo actuar como ingeniero responsable?

Cada estación presenta una pregunta clave que los estudiantes deben responder, llevando a la propuesta final: **EduConecta Aburrá Sur**.

## 📁 Estructura del Proyecto

```
el-viaje-profesional/
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias Python
├── config/
│   ├── video_config.json             # Configuración del video
│   └── estaciones.json               # Datos de las 4 estaciones
├── scripts/
│   ├── generate_video.py             # Script principal para generar video
│   └── utils.py                      # Funciones auxiliares
├── assets/
│   ├── backgrounds/                  # Imágenes de fondo
│   ├── logos/                        # Logos del TdeA y EduConecta
│   ├── fonts/                        # Fuentes personalizadas
│   └── music/                        # Música de fondo
├── video_final/                      # Carpeta de salida
└── docs/
    └── script.md                     # Script completo
```

## 🚀 Requisitos

- Python 3.8+
- FFmpeg instalado en el sistema
- moviepy
- PIL (Pillow)
- numpy

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/anavallejohenao-commits/el-viaje-profesional.git
cd el-viaje-profesional
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Descarga FFmpeg si no lo tienes:
   - **Windows:** `choco install ffmpeg`
   - **Mac:** `brew install ffmpeg`
   - **Linux:** `sudo apt-get install ffmpeg`

## 🎬 Generación del Video

Ejecuta el script principal:

```bash
python scripts/generate_video.py
```

El video se generará en la carpeta `video_final/el_viaje_profesional.mp4`

## ⚙️ Configuración

Edita `config/video_config.json` para personalizar:
- Resolución (720p, 1080p, etc.)
- Duración de transiciones
- Colores de las estaciones
- Velocidad de reproducción

## 📝 Contenido del Video

El video incluye:
- **Presentadores:** Ana Sofía y Juan Diego alternando
- **4 Estaciones** con transiciones visuales
- **Títulos dinámicos** con colores específicos (verde para impares, azul para pares)
- **Secciones:** Introducción, 4 estaciones, presentación de solución, cierre
- **Duración aproximada:** 20-25 minutos

## 🎨 Estilos Visuales

- **Estaciones Pares (Verde 🟢):** Formación Integral, Ruta Académica
- **Estaciones Impares (Azul 🔵):** Competencias en Acción, Impacto Social
- **Transiciones:** Fundidos, deslizamientos y efectos de texto
- **Tipografía:** Profesional y clara para audiencia educativa

## 👥 Créditos

- **Concepto y Guión:** Ana Sofía Vallejo Henao, Juan Diego Romero
- **Institución:** TdeA Aburrá Sur
- **Proyecto:** EduConecta Aburrá Sur

## 📄 Licencia

Creative Commons - TdeA Aburrá Sur

---

**Última actualización:** Septiembre 2026