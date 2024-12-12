from pvrecorder import PvRecorder
import wave, struct


# for index, device in enumerate(PvRecorder.get_available_devices()):
#     print(f"{index} - {device}") 

#output 
# 0 - Microphone (Logi USB Headset) vamos a usar este
# 1 - Microphone Array (Realtek(R) Audio)

recorder = PvRecorder(device_index = 0, frame_length = 512 )
audio = []
path = "./audio/recording.wav"

try: 
    recorder.start()
    while True:
        frame = recorder.read()
        audio.extend(frame)

except KeyboardInterrupt:
    recorder.stop()

    with wave.open(path, 'w') as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack('h' * len(audio), *audio))
finally:
    recorder.delete()
