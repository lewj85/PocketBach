import threading
import pyaudio
import wave


# initialize variables
FORMAT = pyaudio.paInt16
CHANNELS = 2            # stereo
RATE = 44100            # framerate in Hz
CHUNK = 1024            # frames per buffer
RECORD_SECONDS = 10     # 10 seconds max
WAVE_OUTPUT_FILENAME = "melody.wav"


# record() function definition
def record(event):
    audio = pyaudio.PyAudio()

    # start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("\nRecording...")
    frames = []

    # continue recording while event (Enter key) has not occurred
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


# main() function
def main():
    # create recording event for multithreading
    event = threading.Event()
    thread = threading.Thread(target=record, args=(event,))
    thread.start()

    # check for Enter key to be pressed while still recording
    input("Press Enter to stop recording.")
    event.set()
    thread.join()
    print("Recording complete.")


# call main()
if __name__ == "__main__":
    print('Audio Recorder - by Jesse Lew\n\n')
    main()
