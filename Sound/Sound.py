import numpy as np
from pydub import AudioSegment
from scipy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt

class Sound:
    def __init__(self, path: str):
        self.path: str = path
        self.originSound: AudioSegment = AudioSegment.from_wav(path)
        self.monoSound: AudioSegment = self.originSound.set_channels(1)
        self.SAMPLE_RATE = self.originSound.frame_rate
        self.DURATION = self.originSound.duration_seconds
        self.nSampleNormalised = int(self.SAMPLE_RATE * self.DURATION)
        self.yf = rfft(np.array(self.monoSound.get_array_of_samples()))
        self.xf = rfftfreq(self.nSampleNormalised, 1/self.SAMPLE_RATE)

    def test(self):
        self.sample = self.monoSound[:1000]
        self.SAMPLE_RATE = self.sample.frame_rate
        self.DURATION = self.sample.duration_seconds
        self.nSampleNormalised = int(self.SAMPLE_RATE * self.DURATION)
        self.yf = rfft(np.array(self.sample.get_array_of_samples()))
        self.xf = rfftfreq(self.nSampleNormalised, 1/self.SAMPLE_RATE)


