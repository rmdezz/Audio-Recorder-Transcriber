from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os

class TranscriptionService:
    def __init__(self):
        # Cargar variables de entorno
        load_dotenv()
        
        # Obtener API key del entorno
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("No se encontró OPENAI_API_KEY en las variables de entorno")
            
        self.client = OpenAI(api_key=api_key)

    def transcribe_and_translate(self, audio_file: Path):
        """Transcribe and translate audio file using OpenAI Whisper API"""
        if not audio_file or not audio_file.exists():
            print("✗ No se encontró el archivo de audio.")
            return

        try:
            print("\n=== Iniciando transcripción ===")
            print(f"✓ Archivo a transcribir: {audio_file.absolute()}")
            
            print("\nTranscribiendo audio...")
            transcription_result = self._transcribe_audio(audio_file)
            
            if transcription_result:
                detected_language = transcription_result.language
                original_text = transcription_result.text
                
                print(f"\n✓ Idioma detectado: {detected_language}")
                
                if detected_language != "en":
                    translation = self._translate_audio(audio_file)
                    if translation:
                        print("\n=== Resultados ===")
                        print(f"Transcripción original: {original_text}")
                        print(f"Traducción al inglés: {translation}")
                else:
                    print("\n=== Resultados ===")
                    print(f"Transcripción: {original_text}")
                    
        except Exception as e:
            print("\n✗ Error crítico durante el proceso:")
            print(f"Tipo de error: {type(e).__name__}")
            print(f"Mensaje: {str(e)}")
            import traceback
            print("\nTraceback completo:")
            traceback.print_exc()
        finally:
            # Asegurarnos de limpiar cualquier recurso pendiente
            self.client = None

    def _transcribe_audio(self, audio_file: Path):
        """Transcribe audio file using OpenAI Whisper API"""
        try:
            with open(audio_file, "rb") as audio:
                transcription = self.client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio,
                    response_format="verbose_json"
                )
            print("✓ Transcripción completada exitosamente")
            return transcription
        except Exception as e:
            print(f"✗ Error durante la transcripción: {str(e)}")
            return None

    def _translate_audio(self, audio_file: Path):
        """Translate audio file to English using OpenAI Whisper API"""
        try:
            with open(audio_file, "rb") as audio:
                translation = self.client.audio.translations.create(
                    model="whisper-1",
                    file=audio,
                    response_format="text"
                )
            return translation
        except Exception as e:
            print(f"✗ Error durante la traducción: {str(e)}")
            return None