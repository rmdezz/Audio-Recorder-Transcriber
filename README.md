# Audio Recorder & Transcriber

Un programa en Python que graba audio desde el micrófono y utiliza la API de OpenAI (Whisper) para transcribir y traducir el audio automáticamente. El programa detecta el idioma del audio y, si no está en inglés, proporciona tanto la transcripción original como su traducción al inglés.

## Características

- Grabación de audio desde el micrófono
- Detección automática del idioma
- Transcripción del audio usando OpenAI Whisper
- Traducción automática al inglés si el audio está en otro idioma
- Almacenamiento automático de las grabaciones con marcas de tiempo
- Interfaz de línea de comandos simple

## Requisitos Previos

- Python 3.10 o superior
- pipenv
- Una API key de OpenAI
- PyAudio (requiere portaudio)

En macOS, puedes instalar portaudio con:
```bash
brew install portaudio
```

## Instalación

1. Clona el repositorio:
```bash
git clone [URL-del-repositorio]
cd [nombre-del-directorio]
```

2. Instala las dependencias usando pipenv:
```bash
pipenv install
```

3. Crea un archivo `.env` en la raíz del proyecto:
```bash
OPENAI_API_KEY=tu_api_key_de_openai
```

## Uso

1. Inicia el programa:
```bash
pipenv run start
```

2. El programa te indicará que presiones Enter para comenzar a grabar.

3. Presiona Enter nuevamente cuando quieras detener la grabación.

4. El programa automáticamente:
   - Guardará el archivo de audio en la carpeta `recordings`
   - Transcribirá el audio
   - Detectará el idioma
   - Si no está en inglés, proporcionará una traducción
   - Mostrará los resultados en la terminal

## Estructura del Proyecto

```
proyecto/
├── .env                    # Variables de entorno (API key)
├── .gitignore             
├── Pipfile                # Dependencias del proyecto
├── README.md              
├── audio_recorder.py      # Clase para manejar la grabación de audio
├── transcription_service.py # Servicio de transcripción usando OpenAI
└── main.py                # Punto de entrada de la aplicación
```

## Ejemplo de Salida

```
Presiona Enter para comenzar a grabar...
Grabando... Presiona Enter nuevamente para detener.

Grabación guardada en: recordings/grabacion_20241220_095649.wav
=== Iniciando transcripción ===
✓ Archivo a transcribir: [ruta_del_archivo]
Transcribiendo audio...
✓ Transcripción completada exitosamente
✓ Idioma detectado: spanish
=== Resultados ===
Transcripción original: [texto en español]
Traducción al inglés: [texto en inglés]

Proceso completado. ¡Hasta luego!
```

## Desarrollo

Este proyecto utiliza:
- `pyaudio` para la grabación de audio
- `openai` para la transcripción y traducción
- `python-dotenv` para la gestión de variables de entorno
- `wave` para el manejo de archivos de audio

## Notas

- Las grabaciones se guardan automáticamente en la carpeta `recordings` con marcas de tiempo
- Se requiere una API key válida de OpenAI para la transcripción y traducción
- El programa maneja automáticamente la detección del idioma y la traducción
