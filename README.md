# neko_sis_uwu
Practica 04 - Comprensión sobre uso de clases, creación de plantillas para la creación de 'entitys', buenas practicas de desarrollo de juegos 2d

Folders
│
├── assets/                  # Carpeta para almacenar recursos del juego (imágenes, sonidos, etc.)
│   ├── images/              # Carpeta para imágenes
│   ├── sounds/              # Carpeta para archivos de sonido
│   ├── fonts/               # Carpeta para fuentes
│   ├── levels/              # Carpeta para datos de niveles
│   └── ...
│
├── src/                     # Carpeta para almacenar el código fuente del juego
│   ├── __init__.py          # Archivo de inicialización del paquete src
│   ├── game.py              # Archivo principal del juego
│   ├── player.py            # Archivo de definición de la clase Player
│   ├── enemy.py             # Archivo de definición de la clase Enemy (si es necesario)
│   ├── screens/             # Carpeta para pantallas o menús del juego
│   │   ├── __init__.py      # Archivo de inicialización de la subcarpeta screens
│   │   ├── start_screen.py  # Archivo para la pantalla de inicio
│   │   ├── game_screen.py   # Archivo para la pantalla de juego
│   │   ├── pause_screen.py  # Archivo para la pantalla de pausa
│   │   └── ...
│   ├── utils/               # Carpeta para módulos de utilidad
│   │   ├── __init__.py      # Archivo de inicialización de la subcarpeta utils
│   │   ├── collision.py     # Archivo con funciones de detección de colisiones
│   │   ├── math_utils.py    # Archivo con funciones matemáticas útiles
│   │   └── ...
│   └── ...
│
├── data/                    # Carpeta para almacenar datos adicionales del juego
│   ├── config.ini           # Archivo de configuración
│   ├── level1.txt           # Datos del nivel 1
│   ├── level2.txt           # Datos del nivel 2
│   └── ...
│
├── tests/                   # Carpeta para pruebas unitarias y de integración
│   ├── test_collision.py    # Archivo con pruebas de detección de colisiones
│   ├── test_math_utils.py   # Archivo con pruebas de funciones matemáticas
│   └── ...
│
└── main.py                  # Archivo principal para ejecutar el juego


# Install 

Frist : python -m venv my_env
Second : .\my_env\Scripts\activate
Third :  pip install pygame

(Remenber : To go .gitignore write, "my_env/", to ignored)