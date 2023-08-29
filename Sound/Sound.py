import numpy as np
from pydub import AudioSegment
from scipy.fft import rfft, rfftfreq
from scipy.signal import find_peaks_cwt

class Sound:
    def __init__(self, path: str):
        self.path: str = path
        self.originSound: AudioSegment = AudioSegment.from_wav(path)
        self.monoSound: AudioSegment = self.originSound.set_channels(1)
        self.SAMPLE_RATE = self.originSound.frame_rate
        self.DURATION = int(self.originSound.duration_seconds)
        self.nSampleNormalised = int(self.SAMPLE_RATE * self.DURATION)
        self.yf = rfft(np.array(self.monoSound.get_array_of_samples()))
        self.xf = rfftfreq(self.nSampleNormalised, 1/self.SAMPLE_RATE)
        self.tblMIDI = np.loadtxt("SoundSample/MIDI_NOTES.txt", delimiter=';')
        self.idxMIDI, self.freqMIDI = np.split(self.tblMIDI, 2, axis=1)

    def getChunk(self, x: int, y: int):
        if 0 <= x < len(self.monoSound) and 0 <= y < len(self.monoSound):
            return self.monoSound[x:y]
        else:
            print("Warning : Bound outside scop")
            return self.monoSound

    def getXf(self, chunk: AudioSegment):
        sample_rate = chunk.frame_rate
        duration = chunk.duration_seconds
        normal = int(sample_rate * duration)
        return rfftfreq(normal, 1/sample_rate)

    def getYf(self, chunk: AudioSegment):
        return rfft(np.array(chunk.get_array_of_samples()))

    def getPeak(self, xf, yf, width, intensity):
        peaks = find_peaks_cwt(yf, width)
        tbl = []
        for i in peaks:
            if yf[i] > intensity:
                tbl.append([self.find_nearest(self.freqMIDI, xf[i])[0], yf[i]])
        return tbl

    def find_nearest(self, array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]







