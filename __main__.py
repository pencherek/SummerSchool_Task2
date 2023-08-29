import matplotlib.pyplot as plt
import numpy as np

from Sound.Sound import Sound

sound = Sound("SoundSample/5.wav")
chunk = sound.getChunk(0, 100)
xf = sound.getXf(chunk)
yf = np.log10(np.abs(sound.getYf(chunk)))
peaks = sound.getPeakIndices(yf, [1, 2, 3])
tbl = []
for i in peaks:
    if yf[i] > 9:
        temp = sound.find_nearest(sound.freqMIDI, xf[i])[0]
        tbl.append([temp, yf[i]])

np.savetxt("SoundSample/dump", tbl, delimiter=',', newline='\n', encoding="utf8", fmt="%0.2f")#, fmt="%3.0f"

#Get the MIDI number from frequence
print(np.where(sound.tblMIDI == sound.find_nearest(sound.freqMIDI, 440))[0][0])


#plt.plot(xf, yf)
#plt.show()
