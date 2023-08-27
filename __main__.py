import matplotlib.pyplot as plt
import numpy as np
from Sound.Sound import Sound

sound = Sound("SoundSample/5.wav")
#sound.test()
for i in range(999):
    print(f"x : {sound.xf[i]}\ny : {np.abs(sound.yf[i])}")




