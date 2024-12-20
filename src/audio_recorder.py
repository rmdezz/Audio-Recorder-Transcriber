import pyaudio
import wave
from datetime import datetime
from pathlib import Path
import threading

class AudioRecorder:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.recording = False
        self.frames = []
        self.p = None
        self.stream = None
        self._recording_thread = None

    def start_recording(self):
        """Start recording audio"""
        self.recording = True
        self.frames = []
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK
        )
        
        # Iniciar el thread de grabación
        self._recording_thread = threading.Thread(target=self._record)
        self._recording_thread.start()

    def _record(self):
        """Thread interno para grabar"""
        while self.recording:
            try:
                data = self.stream.read(self.CHUNK, exception_on_overflow=False)
                self.frames.append(data)
            except Exception as e:
                print(f"Error durante la grabación: {e}")
                self.recording = False
                break

    def stop_recording(self):
        """Stop recording and save the audio file"""
        if not self.recording:
            return None
            
        self.recording = False
        
        # Esperar a que el thread de grabación termine
        if self._recording_thread and self._recording_thread.is_alive():
            self._recording_thread.join()
        
        if self.stream:
            try:
                self.stream.stop_stream()
                self.stream.close()
            except Exception as e:
                print(f"Error al cerrar el stream: {e}")
        
        if self.p:
            try:
                self.p.terminate()
            except Exception as e:
                print(f"Error al terminar PyAudio: {e}")

        if not self.frames:
            print("No hay datos de audio para guardar")
            return None

        return self._save_audio_file()

    def cleanup(self):
        """Limpieza explícita de recursos"""
        if self.recording:
            self.stop_recording()
        
        # Asegurarse de que el thread termine
        if self._recording_thread and self._recording_thread.is_alive():
            self._recording_thread.join()

    def _save_audio_file(self):
        """Save the recorded audio to a file"""
        recordings_dir = Path("recordings")
        recordings_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = recordings_dir / f"grabacion_{timestamp}.wav"

        try:
            wf = wave.open(str(filename), 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            print(f"\nGrabación guardada en: {filename}")
            print(f"Ruta absoluta del archivo de audio: {filename.resolve()}")
            return filename
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
            return None