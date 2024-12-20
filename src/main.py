import sys
import threading
from audio_recorder import AudioRecorder
from transcription_service import TranscriptionService

def main():
    recorder = None
    try:
        recorder = AudioRecorder()
        transcription_service = TranscriptionService()

        print("\nPresiona Enter para comenzar a grabar...")
        input()  # Esperar Enter para iniciar
        
        print("Grabando... Presiona Enter nuevamente para detener.")
        # Iniciar la grabación
        recorder.start_recording()
        
        # Wait for Enter key to stop recording
        input()
        
        # Stop recording and get the filename
        audio_file = recorder.stop_recording()
        
        if audio_file:
            print("\nProcesando el audio...")
            # Transcribe and translate the audio
            transcription_service.transcribe_and_translate(audio_file)
        
        print("\nProceso completado. ¡Hasta luego!")
        
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")
    finally:
        # Limpieza explícita de recursos
        if recorder:
            recorder.cleanup()
        # Terminar el programa
        sys.exit(0)

if __name__ == "__main__":
    main()