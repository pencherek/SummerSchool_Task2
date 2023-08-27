import numpy as np
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq

class SumTest():
    def __int__(self):
        print("OK")

    def test(self):
        print("OK")

    def testpydub(self):
        print("Pydub test start")
        wav_file = AudioSegment.from_wav(file = "SoundSample/sample_piano_1.wav")
        print(wav_file.frame_rate)
        print(wav_file.channels)
        print(wav_file.sample_width)
        print(wav_file.max)
        print(len(wav_file))
        print(wav_file.duration_seconds)
        print("Pydub test end")

    def testfft(self):
        print("fft test start")
        wav_file = AudioSegment.from_wav(file = "SoundSample/5.wav")
        wav_file = wav_file.set_channels(1)
        SAMPLE_RATE = wav_file.frame_rate
        DURATION = wav_file.duration_seconds
        # Number of samples in normalized_tone
        N = int(SAMPLE_RATE * DURATION)
        yf = rfft(np.array(wav_file.get_array_of_samples()))
        xf = rfftfreq(N, 1/SAMPLE_RATE)
        plt.plot(xf, np.abs(yf))
        plt.show()
        print("fft test end")


