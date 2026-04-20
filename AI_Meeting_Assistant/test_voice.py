import sounddevice as sd

for i, dev in enumerate(sd.query_devices()):
    print(i, dev['name'], dev['max_input_channels'], dev['max_output_channels'])