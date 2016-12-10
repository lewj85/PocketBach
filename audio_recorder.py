import threading
import pyaudio
import wave


FORMAT = pyaudio.paInt16
CHANNELS = 2                        # stereo
RATE = 44100                        # framerate in Hz
CHUNK = 1024                        # frames per buffer
RECORD_SECONDS = 10                 # 10 seconds max
WAVE_OUTPUT_FILENAME = "melody.wav"


def record(event):
    audio = pyaudio.PyAudio()

    # start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []

    while not event.wait(0):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Finished recording")
    
    # stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    # write wavefile
    print("Writing file...")
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


def main():
  event = threading.Event()
  thread = threading.Thread(target=record, args=(event,))
  thread.start()

  input("Press Enter to stop recording.")
  event.set()
  thread.join()
  print("Recording complete.")


main()